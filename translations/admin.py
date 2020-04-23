from adminsortable.admin import SortableTabularInline, SortableAdmin
from django.contrib import admin
from django.urls import reverse
from django.utils.safestring import mark_safe
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from reversion.admin import VersionAdmin

from .forms import PhraseForm
from .models import Language, Category, Phrase, Translation, Contributor, PhraseCategory, UserType, TranslationFeedback


@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    list_display = ['name', 'native_name', 'code', 'is_active']
    search_fields = ['name', 'native_name', 'code']
    readonly_fields = ['created_at', 'updated_at']
    list_filter = ['is_active']


class PhraseInlineAdmin(SortableTabularInline):
    model = PhraseCategory
    fields = ['content', 'change_link']
    readonly_fields = ['content', 'change_link']
    extra = 0

    def content(self, obj):
        return obj.phrase.content

    def change_link(self, obj):
        url = reverse('admin:translations_phrase_change', args=(obj.phrase_id,))
        return mark_safe('<a href="%s">Edit</a>' % url)


@admin.register(Category)
class CategoryAdmin(SortableAdmin):
    list_display = ['name', 'parent_category', 'is_active']
    search_fields = ['name']
    list_filter = ['parent_category', 'intended_for', 'is_active']
    readonly_fields = ['created_at', 'updated_at']
    filter_horizontal = ['intended_for']
    inlines = [PhraseInlineAdmin]


class TranslationInlineAdmin(admin.StackedInline):
    model = Translation
    fields = ['language', 'content', 'special_note', 'audio_clip']
    extra = 0
    readonly_fields = ['created_at', 'updated_at']


class TranslationFeedbackInline(admin.StackedInline):
    model = TranslationFeedback
    fields = ['name', 'whats_wrong', 'suggestion']
    extra = 0


@admin.register(Translation)
class TranslationAdmin(admin.ModelAdmin):
    search_fields = ['translation__phrase__summary', 'translation__phrase', 'content']
    list_display = ['content']
    inlines = [TranslationFeedbackInline]


class PhraseResource(resources.ModelResource):
    class Meta:
        model = Phrase
        exclude = ['id']


@admin.register(Phrase)
class PhraseAdmin(ImportExportModelAdmin, VersionAdmin):
    list_display = ['summary', 'content', 'updated_at']
    search_fields = ['summary', 'content']
    inlines = [TranslationInlineAdmin]
    form = PhraseForm
    readonly_fields = ['created_at', 'updated_at']
    resource_class = PhraseResource
    ordering = ['order']


@admin.register(Contributor)
class ContributorAdmin(VersionAdmin):
    list_display = ['name']
    search_fields = ['name']
    readonly_fields = ['created_at', 'updated_at']


@admin.register(UserType)
class UserTypeAdmin(VersionAdmin):
    list_display = ['name', 'is_active']
    search_fields = ['name']
    list_filter = ['is_active']
    readonly_fields = ['created_at', 'updated_at']
