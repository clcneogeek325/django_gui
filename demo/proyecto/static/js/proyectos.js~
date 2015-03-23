// prepare the form when the DOM is ready 
var nombre_tabla = "#tabla_proyectos"; // id
var nombre_boton_eliminar = ".delete"; // Clase
var nombre_formulario_modal = "#frmEliminar"; //id
var nombre_ventana_modal = "#ModalDelete"; //

$(document).ready(function() { 
      $(nombre_boton_eliminar).on('click',function(e){
            e.preventDefault();
            var Pid = $(this).attr('id');
            var name = $(this).data('name');
            $('#modal_idProducto').val(Pid);
            $('#modal_name').text(name);
        });

    var optionsDelete = {
          success:showResponseDelete
          };
          
    var optionsCreate = { 
         target:        '#id_nombre',   // target element(s) to be updated with server response 
         success:       showResponseCreate  // post-submit callback 
         }; 
  
    $('#frProyecto').ajaxForm(optionsCreate);
    $(nombre_formulario_modal).ajaxForm(optionsDelete); 
}); 
 
 
function showResponseDelete(response){ 
        if(response.status=="True"){
                        alert("Eliminado!");
                        var idProd = response.product_id;
                        var elementos= $(nombre_tabla+' >tbody >tr').length;
                        if(elementos==1){
                                location.reload();
                        }else{
                            $('#tr'+idProd).remove();
                            $(nombre_ventana_modal).modal('hide');
                        }
                        
                    }else{
                        alert("Hubo un error al eliminar!");
                        $(nombre_ventana_modal).modal('hide');
                    };
        }
function showResponseCreate(response){ 
    if(response.status=="true"){
                        $("#ModalCreate ").modal('hide');
                        $("#lista_proyectos").append(" \
                        <tr id='tr"+response.id+"'>\
							<th scope='row'>"+response.id+"</th> \
						  	<td>"+response.nombre+"</td> \
						 	 <td>"+response.fecha
						 	 +"</td> \
							 <td>\
							 	<button type='button' class='btn btn-info'>Configurar</button> \
							 	<button type='button' class='btn btn-danger'>Eliminar</button> \
							</td> \
  			           </tr>");
					alert("El proyecto se ha creado correctamente!");
      }else{
			$("#ModalCreate").modal('hide');
			alert("Hubo un error al crear el proyecto!");        
			};
} 


