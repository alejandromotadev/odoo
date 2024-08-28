{
    "name": "Hospital Management System Custom Module",
    "author": "Rafael Mota :)",
    "license": "LGPL-3",
    "version": "0.01",
    "category": "Health",
    "website": "https://piaggiomx.com",
    "depends": ["mail"], #Especificamos esta dependencia para trackear las acciones aplicadas al modulo/modelo
    "data":[
        "security/ir.model.access.csv",
        "views/patient_views.xml",
        "views/patient_readonly_view.xml",
        "views/appointment_view.xml",
        "views/menu.xml",
    ]
}