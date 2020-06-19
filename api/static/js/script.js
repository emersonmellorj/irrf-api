
$(document).ready(function () {
    const nome = $("#id_nome")
    const salario_bruto = $("#id_salario_bruto")
    const botao = $("#btn-calcular")

    $(botao).click(() => {
        $(".invalid-feedback").remove()

        if (nome.val() === "") {
            $(nome).addClass("form-control is-invalid")
            $(nome).after("<div class='invalid-feedback'>O nome não pode ser vazio!</div>")
            $(nome).focus();
        }

        if (salario_bruto.val() === "") {
            $(salario_bruto).addClass("form-control is-invalid")
            $(salario_bruto).after("<div class='invalid-feedback'>O salário não pode ser vazio!</div>")
            $(salario_bruto).focus();

        }

        if ((salario_bruto.val()) < 0) {
            $(salario_bruto).addClass("form-control is-invalid")
            $(salario_bruto).after("<div class='invalid-feedback'>O valor do salário não pode ser negativo!</div>")
            $(salario_bruto).focus();
            return false;
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