# Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
# MIT License. See license.txt

from __future__ import unicode_literals
import frappe
from frappe.utils import date_diff, add_months, today, getdate, add_days, flt, get_last_day

def get_context(context):
    customer = frappe.get_doc("Customer", {"email_id": frappe.session.user})
    subscriptions_docs = frappe.get_list('Subscription', fields=["*"], filters={'customer': customer.name})
    subscriptions = []
    l3harris_status_values = []
    for i in subscriptions_docs:
        subscriptions.append(frappe.get_doc("Subscription", i.name))
        if i.l3_status == "Request Sent":
            l3harris_status_values.append(1)
        elif i.l3_status == "Provisioning":
            l3harris_status_values.append(2)
        elif i.l3_status == "Activivating":
            l3harris_status_values.append(3)
        elif i.l3_status == "Done":
            l3harris_status_values.append(4)
    context.customer = customer
    context.subscriptions = subscriptions
    invoices = frappe.get_list('Sales Invoice', fields=["*"], filters={'customer': customer.name}, ignore_permissions=True)
    context.invoices = invoices
    tickets = frappe.get_list('Issue', fields=["*"], filters={'customer': customer.name}, ignore_permissions=True)
    context.tickets = tickets
    context.l3harris_status = ["Request Sent", "Provisioning", "Activivating", "Done"]
    context.l3harris_status_values = l3harris_status_values
    context.throughtput = frappe.db.get_list("Network Throughput", fields=["throughput"], ignore_permissions = True)
    context.latency = frappe.db.get_list("Network Latency", fields = ["network_latency"], ignore_permissions = True)
    context.network_type = frappe.db.get_list("Network Type", fields = ["network_type"], ignore_permissions = True)
    context.locations = frappe.db.get_list("Network Location", fields = ["location"], ignore_permissions = True)
    

    return context

@frappe.whitelist(allow_guest=True)
def get_latency_throughput():
    throughtput = frappe.db.get_list("Network Throughput", order_by="priority", ignore_permissions = True)
    latency = frappe.db.get_list("Network Latency", order_by="priority", ignore_permissions = True)
    return {"throughtput": throughtput , "latency": latency}

@frappe.whitelist(allow_guest=True)
def make_subscription(network_type, network_location, latency, throughput, from_date, to_date):
    customer = frappe.get_doc("Customer", {"email_id": frappe.session.user})
    throughtput_scale = frappe.db.get_list("Network Throughput", order_by="priority", ignore_permissions = True)
    latency_scale = frappe.db.get_list("Network Latency", order_by="priority", ignore_permissions = True)
    latency = latency_scale[int(latency)].name
    throughput = throughtput_scale[int(throughput)].name
    from_date = getdate(from_date)
    to_date = getdate(to_date)
    duration = date_diff(to_date, from_date)
    item = frappe.db.exists("Item", {
                                    "is_l3harris_service": 1,
                                    "network_type": network_type,
                                    "network_location": network_location,
                                    "network_latency": latency,
                                    "network_throughput": throughput
                                })
    if item:
        item = frappe.get_doc("Item", item)
        item_price = frappe.get_doc("Item Price", {"item_code": item.name, "price_list": "Standard Selling"})
    else:
        frappe.throw("The Subscription for the given attr. is not available.")
    
    
    sub_plan = frappe.db.exists("Subscription Plan", {"item": item.name, "billing_interval_count": duration})
    if sub_plan:
        sub_plan = frappe.get_doc("Subscription Plan", sub_plan)
    else:
        sub_plan = frappe.new_doc("Subscription Plan")
        sub_plan.plan_name = item.name + str(duration)
        sub_plan.item = item.name
        sub_plan.price_determination = "Based on price list"
        sub_plan.price_list = "Standard Selling"
        sub_plan.billing_interval_count = duration
        sub_plan.insert(ignore_permissions=True)

    subscription = frappe.new_doc("Subscription")
    subscription.customer = customer.name
    subscription.start = getdate(today())
    subscription.cancel_at_period_end = 1
    subscription.append("plans", {
            "qty": int(duration)*24,
            "plan": sub_plan.name,
        })
    subscription.tax_template = "US ST 6% - L"
    subscription.generate_invoice_at_period_start = 1
    subscription.insert(ignore_permissions=True)
    estimate = float(item_price.price_list_rate) * int(duration)*24
    print(estimate)
    return estimate

@frappe.whitelist(allow_guest=True)
def make_estimate(network_type, network_location, latency, throughput, from_date, to_date):
    customer = frappe.get_doc("Customer", {"email_id": frappe.session.user})
    throughtput_scale = frappe.db.get_list("Network Throughput", order_by="priority", ignore_permissions = True)
    latency_scale = frappe.db.get_list("Network Latency", order_by="priority", ignore_permissions = True)
    latency = latency_scale[int(latency)].name
    throughput = throughtput_scale[int(throughput)].name
    from_date = getdate(from_date)
    to_date = getdate(to_date)
    duration = date_diff(to_date, from_date)
    item = frappe.db.exists("Item", {
                                    "is_l3harris_service": 1,
                                    "network_type": network_type,
                                    "network_location": network_location,
                                    "network_latency": latency,
                                    "network_throughput": throughput
                                })
    if item:
        item = frappe.get_doc("Item", item)
        item_price = frappe.get_doc("Item Price", {"item_code": item.name, "price_list": "Standard Selling"})
    else:
        frappe.throw("The Subscription for the given attr. is not available.")
    
    

    estimate = float(item_price.price_list_rate) * int(duration)*24
    return estimate

@frappe.whitelist(allow_guest=True)
def make_ticket(subject, desc, subsc):
    ticket = frappe.new_doc("Issue")
    customer = frappe.get_doc("Customer", {"email_id": frappe.session.user})
    ticket.subject = subject
    ticket.customer = customer.name
    ticket.description = desc
    ticket.subscription = subsc
    ticket.save(ignore_permissions=True)