{
    "name": "Hospital Management System Custom Module",
    "author": "Rafael Mota :)",
    "license": "LGPL-3",
    "version": "0.01",
    "category": "Health",
    "website": "https://piaggiomx.com",
    "depends": ["mail"], #Especificamos "mail" para trackear las modificaciones al modulo/modelo
    "data":[
        "security/ir.model.access.csv",
        "data/sequence.xml",
        "views/patient_views.xml",
        "views/patient_readonly_views.xml",
        "views/appointment_views.xml",
        "views/patient_tag_views.xml",
        "views/menu.xml",
    ]
}