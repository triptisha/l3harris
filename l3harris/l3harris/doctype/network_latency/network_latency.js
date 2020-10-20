// Copyright (c) 2020, Rahi Systems Pvt Ltd and contributors
// For license information, please see license.txt

frappe.ui.form.on('Network Latency', {
	refresh: function(frm) {

	},
	network_latency: function (frm) {
		var val = frm.doc.network_latency;
		let isnum = /^\d+$/.test(val);
		if (isnum) {
			val = String(val)+String("ms");
			frm.set_value("network_latency", val);
			// frm.refresh_field("network_latency");
		}
	}
});
