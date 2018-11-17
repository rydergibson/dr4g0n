function dr4g0n() {
   forms = document.getElementsByTagName('form');
   for (var i = 0; i < forms.length; i++) {
      console.log(forms[i].action);
      inputs = forms[i].getElementsByTagName('input');
      for (var x = 0; x < inputs.length; x++) {
         if (inputs[x].name !== "") {
            console.log(inputs[x].name);
         }
      }
      console.log(forms[i].method);
   }
}
dr4g0n();
