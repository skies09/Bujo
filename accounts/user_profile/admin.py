from django.contrib import admin
from accounts.user_profile.models import Affirmation, Gratitude, Passion, FavoriteThing, About


@admin.register(Affirmation)
class AffirmationAdmin(admin.ModelAdmin):
    list_display = ['user', 'text', 'is_active', 'order', 'created']
    list_filter = ['is_active', 'created', 'updated']
    search_fields = ['user__username', 'user__name', 'text']
    list_editable = ['is_active', 'order']
    readonly_fields = ['public_id', 'created', 'updated']
    ordering = ['user', 'order', 'created']


@admin.register(Gratitude)
class GratitudeAdmin(admin.ModelAdmin):
    list_display = ['user', 'text', 'is_active', 'order', 'created']
    list_filter = ['is_active', 'created', 'updated']
    search_fields = ['user__username', 'user__name', 'text']
    list_editable = ['is_active', 'order']
    readonly_fields = ['public_id', 'created', 'updated']
    ordering = ['user', 'order', 'created']


@admin.register(Passion)
class PassionAdmin(admin.ModelAdmin):
    list_display = ['user', 'text', 'is_active', 'order', 'created']
    list_filter = ['is_active', 'created', 'updated']
    search_fields = ['user__username', 'user__name', 'text']
    list_editable = ['is_active', 'order']
    readonly_fields = ['public_id', 'created', 'updated']
    ordering = ['user', 'order', 'created']


@admin.register(FavoriteThing)
class FavoriteThingAdmin(admin.ModelAdmin):
    list_display = ['user', 'category', 'title', 'is_active', 'order', 'created']
    list_filter = ['category', 'is_active', 'created', 'updated']
    search_fields = ['user__username', 'user__name', 'title', 'description']
    list_editable = ['is_active', 'order']
    readonly_fields = ['public_id', 'created', 'updated']
    ordering = ['user', 'category', 'order', 'created']


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ['user', 'nickname', 'location', 'occupation', 'is_public', 'created']
    list_filter = ['is_public', 'created', 'updated']
    search_fields = ['user__username', 'user__name', 'nickname', 'location', 'occupation']
    list_editable = ['is_public']
    readonly_fields = ['public_id', 'created', 'updated']
    ordering = ['user', 'created']
    
    fieldsets = (
        ('User Information', {
            'fields': ('user', 'nickname', 'pronouns', 'location', 'occupation', 'education')
        }),
        ('Personal Details', {
            'fields': ('personality_type', 'zodiac_sign', 'life_goals', 'personal_mission')
        }),
        ('Interests & Lifestyle', {
            'fields': ('hobbies', 'interests', 'lifestyle_preferences')
        }),
        ('Personal Story', {
            'fields': ('personal_story', 'achievements', 'challenges_overcome')
        }),
        ('Values & Beliefs', {
            'fields': ('core_values', 'beliefs', 'philosophy')
        }),
        ('Social & Relationships', {
            'fields': ('relationship_status', 'family_info', 'social_preferences')
        }),
        ('Professional', {
            'fields': ('career_goals', 'skills', 'work_style')
        }),
        ('Health & Wellness', {
            'fields': ('health_goals', 'fitness_preferences', 'wellness_practices')
        }),
        ('Creative & Expression', {
            'fields': ('creative_interests', 'artistic_preferences', 'self_expression')
        }),
        ('Future & Dreams', {
            'fields': ('bucket_list', 'dreams_aspirations', 'future_plans')
        }),
        ('Additional', {
            'fields': ('notes', 'is_public')
        }),
    )
