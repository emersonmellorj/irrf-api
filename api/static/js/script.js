
const nome = $("#id_nome");
const salario_bruto = $("#id_salario_bruto");
const dependentes = $("#id_numero_deps");
const botao = $("#btn-calcular");
const resultado = $("#resultado");

$(document).ready(function () {

    $(botao).click(() => {
        $(".invalid-feedback").remove()

        if (nome.val() === "") {
            $(nome).addClass("form-control is-invalid")
            $(nome).after("<div class='invalid-feedback'>O nome não pode ser vazio!</div>")
            $(nome).focus();
            return false;
        }

        else if (salario_bruto.val() === "") {
            $(salario_bruto).addClass("form-control is-invalid")
            $(salario_bruto).after("<div class='invalid-feedback'>O salário não pode ser vazio!</div>")
            $(salario_bruto).focus();
            return false;

        }

        else if ((salario_bruto.val()) < 0) {
            $(salario_bruto).addClass("form-control is-invalid")
            $(salario_bruto).after("<div class='invalid-feedback'>O valor do salário não pode ser negativo!</div>")
            $(salario_bruto).focus();
            return false;
        }

        else {

            (function ($) {
                /* Chama a API para realizar os calculos e devolver os valores solicitados */
                $.ajax({
                    type: 'post',
                    url: 'api/v1/irrf/resultado',
                    data: {
                        'nome': nome.val(),
                        'salario_bruto': salario_bruto.val(),
                        'numero_deps': dependentes.val(),
                        'javascript': true,
                        'csrfmiddlewaretoken': window.CSRF_TOKEN
                    },
                    success: function (data) {
                        console.log('DATA SUCCESS: ' + data.mensagem);
                        resultado.addClass('alert alert-success mt-4');
                        resultado.html('<markdown>' + data.mensagem + '</markdown>');
                        $("#form").trigger("reset");
                        nome.removeClass("is-valid");
                        salario_bruto.removeClass("is-valid");
                    },
                    error: function (xhr, status, error) {
                        // shit happens friends!
                        console.log('DATA ERROR: ' + xhr + status + error)
                    }
                });
            }(jQuery));
        }

    })

    $(nome).change(() => {
        if ((nome.val() !== "")) {
            $(nome).removeClass("is-invalid")
            $(nome).addClass("form-control is-valid")
            $(nome).focus();
        }
    })

    $(salario_bruto).change(() => {
        $(".invalid-feedback").remove()

        if ((salario_bruto.val()) < 0) {
            $(salario_bruto).addClass("form-control is-invalid")
            $(salario_bruto).after("<div class='invalid-feedback'>O valor do salário não pode ser negativo!</div>")
            $(salario_bruto).focus();
        }

        else if (salario_bruto.val() === "") {
            $(salario_bruto).addClass("form-control is-invalid")
            $(salario_bruto).after("<div class='invalid-feedback'>O salário não pode ser vazio!</div>")
            $(salario_bruto).focus();
        }
        else {
            $(salario_bruto).removeClass("is-invalid")
            $(salario_bruto).addClass("form-control is-valid")
        }

    });

})