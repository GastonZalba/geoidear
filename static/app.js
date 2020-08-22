'use strict';
(
    function () {

        const results = document.getElementById('results');
        const resultsCnt = results.textContent;

        const form = document.forms[0];
        const cleanBtn = document.getElementById('cleanForm');
        const fillBtn = document.getElementById('fillExample');
        const copyBtn = document.getElementById('copyValues');
        const responseTypeSel = form.elements.responseType;
        const loadingDiv = '<div class="lds-circle"><div></div></div>';


        const showError = function (error) {
            results.classList.add('error');
            results.innerHTML = JSON.stringify(error, undefined, 2);
        }

        const showLoading = function () {           
            results.innerHTML = loadingDiv;
        }

        const showResults = function (data) {
            results.classList.remove('error');
            if (getResponseType() === 'json')
                data = JSON.stringify(data, undefined, 2);
            else
                data = data.replace(/\n/g, '\n').replace(/,/g, '\t');

            results.innerHTML = data;
        }

        const cleanResults = function () {
            results.classList.remove('error');
            results.textContent = resultsCnt;
        }

        const getResponseType = function () {
            return responseTypeSel.options[responseTypeSel.selectedIndex].value;
        }

        const forceDownload = function (blob) {
            let url = window.URL.createObjectURL(blob);
            let a = document.createElement('a');
            a.href = url;
            a.download = "geoidear-api.csv";
            document.body.appendChild(a);
            a.click();
            a.remove();
        }

        const sendData = async function (formData) {

            try {

                let response = await fetch('./convert', {
                    method: "POST",
                    body: formData
                });

                if (response.status !== 200) {

                    response = await response.json();
                    return showError(response)

                }

                if (getResponseType() === 'csv') {

                    response = await response.blob();
                    forceDownload(response);
                    cleanResults();

                } else {

                    response = await response.json();
                    return showResults(response);
                }
            } catch (err) {
                showError(err);
                console.error(err);
            }


        }

        const submitForm = async function () {
            let formData = new FormData(form);
            await sendData(formData);
            form.submitForm.disabled = false;
        }

        form.onsubmit = function (e) {
            form.submitForm.disabled = true;
            cleanResults();
            showLoading();
            e.preventDefault();
            submitForm();

        }

        cleanBtn.onclick = function () {
            form.elements.data.value = '';
            cleanResults();
        }

        copyBtn.onclick = function (e) {

            const copyToClipboard = function (text) {
                let dummy = document.createElement("textarea");
                document.body.appendChild(dummy);
                dummy.value = text;
                dummy.select();
                document.execCommand("copy");
                document.body.removeChild(dummy);

            }

            copyToClipboard(results.textContent);
            e.preventDefault();
        }

        fillBtn.onclick = function () {
            form.elements.data.value = `-35.414329, -60.141746
-35.406613, -60.772444
-37.875285, -62.885637
-34.431955, -61.075266
-35.438261, -62.987166
-36.582007, -62.117484`;
        }
    })()