from django import forms
from principal.models import *
from django.utils.translation import ugettext_lazy as _
from django.forms.extras.widgets import SelectDateWidget



class AgendaForm(forms.ModelForm):
    fecha = forms.DateField(widget=SelectDateWidget())
    class Meta:
        model = EntradaAgenda
	#widgets = {'coordx': forms.HiddenInput(),'coordy':forms.HiddenInput() }
        fields = ('titulo', 'descripcion', 'fecha', 'hora' ,'lugar', 'coordx', 'coordy')

    def __init__(self, *args, **kwargs): 
			super(AgendaForm,self).__init__(*args,**kwargs)
			self.fields['coordx'].widget.attrs['readonly'] = True
			self.fields['coordy'].widget.attrs['readonly'] = True



class DiarioForm(forms.ModelForm):
    class Meta:
        model = EntradaDiario
        fields = ( 'titulo', 'texto', 'imagen', 'lugar', 'coordx', 'coordy')
    def __init__(self, *args, **kwargs): 
			super(DiarioForm,self).__init__(*args,**kwargs)
			self.fields['coordx'].widget.attrs['readonly'] = True
			self.fields['coordy'].widget.attrs['readonly'] = True

class FraseComunForm(forms.ModelForm):
    class Meta:
        model = FraseComun
        fields = ('texto',)

class FraseComunFormAdmin(forms.ModelForm):
    class Meta:
        model = FraseComun
        exclude = ('esGeneral','autor',)


class PensamientoForm(forms.ModelForm):
    class Meta:
        model = Pensamientos
        fields = ( 'tipoPensamiento', 'publicacion','coordx', 'coordy')
    def __init__(self, *args, **kwargs): 
			super(PensamientoForm,self).__init__(*args,**kwargs)
			self.fields['coordx'].widget.attrs['readonly'] = True
			self.fields['coordy'].widget.attrs['readonly'] = True
			self.fields['tipoPensamiento'].label="Tipo de pensamiento"

class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ( 'esAnonima','estaOculto','texto','coordx', 'coordy')
    def __init__(self, *args, **kwargs): 
			super(ComentarioForm,self).__init__(*args,**kwargs)
			self.fields['coordx'].widget.attrs['readonly'] = True
			self.fields['coordy'].widget.attrs['readonly'] = True
			self.fields['esAnonima'].label="Marque esta casilla si desea enviar el comentario anonimamente"
			self.fields['estaOculto'].label="Marque esta casilla si desea enviar el comentario oculto(invisible)"


#class perfilForm(Readonly,ModelForm):
class perfilForm(forms.ModelForm):
    class Meta:
        model=Perfil
        exclude =('usuario', 'esVerdadero', 'esActivo')

    def clean_perfil(self):
        perfil = self.cleaned_data["alias"]
        try:
            Perfil.objects.get(alias = alias)
        except Perfil.DoesNotExist:
            return alias
        raise forms.ValidationError("Ya existe un perfil con este alias.")

    def __init__(self,*args,**kwargs):
        super(perfilForm,self).__init__(*args,**kwargs)
        self.fields['coordx'].widget.attrs['readonly'] = True
        self.fields['coordy'].widget.attrs['readonly'] = True
    #class NewMeta:
     #   readonly = ('coordx')





class CaractForm(forms.ModelForm):
    class Meta:
        model=TipoVotacion

class UploadForm(forms.ModelForm):
    class Meta:
        model=Fichero
	exclude=('perfilOrigen','perfilDestino');
    def __init__(self,*args,**kwargs):
        super(UploadForm,self).__init__(*args,**kwargs)
        self.fields['coordx'].widget.attrs['readonly'] = True
        self.fields['coordy'].widget.attrs['readonly'] = True
	self.fields['url'].label="Seleccione el archivo que desea enviar"

class PerfilVisitadoForm(forms.ModelForm):
    class Meta:
        model=PerfilVisitado
	exclude=('perfilOrigen','perfilDestino');

class ComentarioLeidoForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ( 'estaLeido',)

class PassPerdido(forms.ModelForm):
    class Meta:
        model = UsuarioRegistrado
        fields = ( 'email',)

class Votar(forms.ModelForm):
    class Meta:
        model = Votacion





