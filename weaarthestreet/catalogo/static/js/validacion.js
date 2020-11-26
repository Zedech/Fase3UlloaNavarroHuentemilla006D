$(function() 
          {
            $("#gg").validate({
                 rules: {
                        email: {
                            required: true,
                            email: true
                        },
                        nombre: "required",
                        fono: "required",
                        fecha: "required",
                        apellido:"required"    
                    }, //reglas
                messages: {
                    email: {
                        required: 'Ingresa tu correo electrónico',
                        email: 'Formato de correo no válido'
                    },
                    nombre: {
                        required: 'Ingresa su nombre',
                        minlength: 'Caracteres insuficiente'
                    },
                    fono:{
                        required: 'Ingrese un número de celular',
                        minlength: 'Cantidad de digitos insuficiente'
                    },
                    fecha:{
                        required: 'Seleccione una fecha válida',
                        min: 'Fecha no corresponde'
                    },
                    apellido: {
                      required: 'Ingresa su apellido',
                      minlength: 'Caracteres insuficiente'
    
                    }
                }
            }); 
        });
        
    
          $(document).ready(function(){
            $("#mostar").click(function(){
              $("p").toggle();
            });
          });

          $(document).ready(function(){
            $(".alerta").click(function(){
              $("p").hide("slow", function(){
                alert("Sera redirigido a otra pagina");
              });
            });
          });

          $(document).ready(function(){
              $("#oso").click(function(){
                  if ($('#gg').valid()){
                      alert("Formulario enviado");
                  }
              });
          });

          $(document).ready(function(){
            $(".animacion").click(function(){
              $("#plugo").css("color", "white").slideUp(2000).slideDown(2000);
            });
          });

