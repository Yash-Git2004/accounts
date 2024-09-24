from odoo import models, fields

class FormData(models.Model):
    _name = 'form.data'
    _description = 'Form Data'

    date = fields.Date(string='Date')
    designation_category = fields.Char(string='Designation Category')
    hospital_name = fields.Char(string='Hospital Name')
    treatment = fields.Char(string='Treatment')
    employee = fields.Char(string='Employee')
    division_medical_reimbursement_for_suffering_from = fields.Char(string='Division Medical Reimbursement For Suffering From')
    doctor_name = fields.Char(string='Doctor Name')
    amount_in_advance = fields.Float(string='Amount in Advance')
    expenditure_amount = fields.Float(string='Expenditure Amount')
    medicine_ids = fields.One2many('medicine.data', 'form_data_id', string='Medicine Details')

    # New fields for the bottom section
    applied_by = fields.Many2one('res.users', string='Applied By')
    applied_date = fields.Date(string='Applied Date')
    approved_by = fields.Many2one('res.users', string='Approved By')
    approved_date = fields.Date(string='Approved Date')
    rejected_by = fields.Many2one('res.users', string='Rejected By')
    rejected_date = fields.Date(string='Rejected Date')
    cancelled_by = fields.Many2one('res.users', string='Cancelled By')
    cancelled_date = fields.Date(string='Cancelled Date')
    on_hold_by = fields.Many2one('res.users', string='On Hold By')
    on_hold_date = fields.Date(string='On Hold Date')

class MedicineData(models.Model):
    _name = 'medicine.data'
    _description = 'Medicine Data'

    form_data_id = fields.Many2one('form.data', string='Form Data')
    medicine_name = fields.Char(string='Medicine Name')
    dosage = fields.Char(string='Dosage')
    quantity = fields.Integer(string='Quantity')
    sequence = fields.Integer(string='Sequence')
    sr_no = fields.Integer(string="Sr.No")
    price = fields.Float(string="Price")