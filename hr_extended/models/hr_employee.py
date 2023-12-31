# -*- coding:utf-8 -*-
#
#
#    Copyright (C) 2011,2013 Michael Telahun Makonnen <mmakonnen@gmail.com>.
#    All Rights Reserved.
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published
#    by the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
#

from odoo import models, fields


class HrEmployee(models.Model):
    _inherit = 'hr.employee'

    
    fam_education_ids = fields.One2many(
        'hr.employee.education', 'employee_id', "Education")
    fam_experience_ids = fields.One2many(
        'hr.employee.experience', 'employee_id', "Experience")
    hobby = fields.Char("Hobby")
    emp_1 = fields.Char("Emp1")
    talent = fields.Char("Talent")
    fam_spouse = fields.Char("Name")
    fam_spouse_employer = fields.Char("Employer")
    fam_spouse_tel = fields.Char("Telephone.")
    fam_children_ids = fields.One2many(
        'hr.employee.children', 'employee_id', "Children")
    fam_father = fields.Char("Father's Name")
    fam_father_date_of_birth = fields.Date(
        "Date of Birth", oldname='fam_father_dob')
    fam_mother = fields.Char("Mother's Name")
    fam_mother_date_of_birth = fields.Date(
        "Date of Birth", oldname='fam_mother_dob')
    blood_group = fields.Selection([('a', 'Group A'), ('b', 'Group B'), ('o', 'Group O'), ('ab', 'Group AB')])
    weight = fields.Integer("Weight")
    high = fields.Integer("high")
    fam_health_ids = fields.One2many(
        'hr.employee.health', 'employee_id', "Health")
    fam_training_ids = fields.One2many(
        'hr.employee.training', 'employee_id', "Training")
   
