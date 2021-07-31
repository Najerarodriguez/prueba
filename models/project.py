from odoo import models, fields, api
from datetime import datetime, timedelta


class ProjectTelyman(models.Model):
    _name = 'project.telyman'

    name = fields.Char(string='Cod Proyecto:', required=True, index=True)
    cod_sitio = fields.Char(string='Cod Sitio:', required=True)
    nombre_sitio = fields.Char(string='Nombre Sitio:', required=True)
    operador = fields.Selection(
        [("ice", "ICE"), ("claro", "CLARO"), ("Entreprise", "ENTERPRICE"), ("jasec", "JASEC"), ("otro", "OTRO"),
         ("Telefonica", "TELEFONICA")], 'Operadora', required=True)
    tipo_trabajo = fields.Many2one('tipo_trabajo.tipo_trabajo', 'Tipo Trabajo', required=True, ondelete='cascade')
    operador = fields.Selection(
        [("ice", "ICE"), ("claro", "CLARO"), ("Entreprise", "ENTERPRICE"), ("jasec", "JASEC"), ("otro", "OTRO"),
         ("Telefonica", "TELEFONICA")], 'Operadora', required=True)
    ubicacion_Gam_rural = fields.Selection([("gam", "GAM"), ("rural", "Rural")], 'Ubicación')
    ubicacion = fields.Char(string='Dirección:')
    provincia = fields.Selection(
        [('No Especificada', 'NO ESPECIFICADA'), ('san_jose', 'San Jose'), ('alajuela', 'Alajuela'),
         ('cartago', 'Cartago'), ('heredia', 'Heredia'), ('guanacaste', 'Guanacaste'), ('puntarenas', 'Puntarenas'),
         ('limon', 'Limón')], string='Provincia:', required=True)
    nombre_proyecto = fields.Char(string='Nombre Proyecto:', required=True)
    coord_x = fields.Float(string='Coord(x):')
    coord_y = fields.Float(string='Coord(y):')
    proyecto_id = fields.Many2one('product.category', 'Contrato')

