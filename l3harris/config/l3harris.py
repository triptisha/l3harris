from __future__ import unicode_literals
from frappe import _

def get_data():
	return [
		{
			"label": _("L3Harris"),
			"items": [
				{
					"type": "doctype",
					"name": "Network Throughput"
				},
				{
					"type": "doctype",
					"name": "Network Latency"
				},
				{
					"type": "doctype",
					"name": "Network Type"
				},
				{
					"type": "doctype",
					"name": "Network Location"
				},
				{
					"type": "doctype",
					"name": "L3harris Log"
				}
			]
		},
		{
			"label": _("Subscription Management"),
			"items": [
				{
					"type": "doctype",
					"name": "Subscriber",
				},
				{
					"type": "doctype",
					"name": "Subscription Plan",
				},
				{
					"type": "doctype",
					"name": "Subscription"
				},
				{
					"type": "doctype",
					"name": "Subscription Settings"
				}
			]
		}
	]
