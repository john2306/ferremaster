from django import forms

class FormularioContacto(forms.Form): 

     nombre=forms.CharField(label="nombre", required=True)

     celular=forms.CharField(label="celular", required=True)

     email=forms.CharField(label="email" , required=True)

     contenido=forms.CharField(label="contenido" , widget=forms.Textarea)
