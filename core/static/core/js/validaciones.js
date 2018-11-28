$(document).ready(function() {
    $("#clienteFormulario").validate({
        rules: {
            txtRut: {
                required:true,
                minlength:3,
                maxlength:30
            },
            txtNombre: {
                required:true,
                minlength:3,
                maxlength:30
            },
            txtApellido: {
                required:true,
                minlength:3,
                maxlength:30
            },
            cboComuna: {
                required:true
            },
            cboRegion:{
                required:true
            },
            txtDireccion: {
                required:true,
                minlength:3,
                maxlength:150
            },
            txtFechaNacimiento: {
                required:true,
                date:true,
                maxlength:2001
            },
            txttelefono: {
                required:true,
                int: true
            },
            txtcorreo: {
                required:true
            }


        }
    });
});