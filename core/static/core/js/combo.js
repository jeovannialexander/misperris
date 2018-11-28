$(document).ready(function(){
  $("#cboRegion").change(function(){
        //este codigo se ejecuta cuando el usuario seleciona un item del combobox
        var regionId = $("#cboRegion").val();
        //console.log(regionId);
        //enviamos el id al nuestro php
        if(regionId ==""){
            $("#cboComuna").prop("disabled",true);
            $("#itemSeleccionar").prop("selected",true);
            return;
        }

        $.get("combo.php",{id:regionId},function(respuesta){

            //dejamos la respuesta dentro del combobox de la comuna
            $("#cboComuna").html(respuesta);
            $("#cboComuna").prop("disabled",false);
        });
  });
});