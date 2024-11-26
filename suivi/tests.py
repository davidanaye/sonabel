from django.test import TestCase
from .models import Fournisseurs, Plans, Status

class FournisseursModelTest(TestCase):

    def setUp(self):
        # Créer un fournisseur pour les tests
        self.fournisseur = Fournisseurs.objects.create(
            nom_four="Test Fournisseur",
            rccm="RCCM123456",
            ifu="IFU654321",
            telephone1="0123456789",
            email="test@fournisseur.com",
            domaine="IT",
        )

    def test_fournisseur_creation(self):
        # Vérifier que le fournisseur est bien créé
        fournisseur = Fournisseurs.objects.get(nom_four="Test Fournisseur")
        self.assertEqual(fournisseur.nom_four, "Test Fournisseur")
        self.assertEqual(fournisseur.email, "test@fournisseur.com")
    
    def test_champs_non_obligatoires(self):
        # Créer un fournisseur sans les champs non obligatoires
        fournisseur = Fournisseurs.objects.create(nom_four="Fournisseur Minimal")
        self.assertIsNone(fournisseur.rccm)
        self.assertEqual(fournisseur.nom_four, "Fournisseur Minimal")

class PlansModelTest(TestCase):

    def setUp(self):
        # Créer un statut et un plan pour les tests
        self.status = Status.objects.create(nom="Validé")
        self.plan = Plans.objects.create(
            annee=2023,
            statut=self.status,
        )


