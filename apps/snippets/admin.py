from django.contrib import admin
import nested_admin

from .models import Beat, Hihat, Kick, Pattern, Snare, Snippet


class HihatPatternInline(nested_admin.NestedTabularInline):
    model = Pattern
    extra = 1
    exclude = ['snare', 'kick']


class SnarePatternInline(nested_admin.NestedTabularInline):
    model = Pattern
    extra = 1
    exclude = ['hihat', 'kick']


class KickPatternInline(nested_admin.NestedTabularInline):
    model = Pattern
    extra = 1
    exclude = ['hihat', 'snare']


class HihatInline(nested_admin.NestedStackedInline):
    model = Hihat
    extra = 1
    inlines = [HihatPatternInline]


class SnareInline(nested_admin.NestedStackedInline):
    model = Snare
    extra = 1
    inlines = [SnarePatternInline]


class KickInline(nested_admin.NestedStackedInline):
    model = Kick
    extra = 1
    inlines = [KickPatternInline]


class BeatInline(nested_admin.NestedStackedInline):
    model = Beat
    extra = 1
    inlines = [HihatInline, SnareInline, KickInline]


@admin.register(Snippet)
class SnippetAdmin(nested_admin.NestedModelAdmin):
    inlines = [BeatInline]
