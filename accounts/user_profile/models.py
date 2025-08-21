from django.db import models
from django.conf import settings
from accounts.abstract.models import AbstractModel, AbstractManager


class AffirmationManager(AbstractManager):
    pass


class Affirmation(AbstractModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='affirmations')
    text = models.TextField()
    is_active = models.BooleanField(default=True)
    order = models.PositiveIntegerField(default=0)
    
    objects = AffirmationManager()
    
    class Meta:
        ordering = ['order', 'created']
        unique_together = ['user', 'text']
    
    def __str__(self):
        return f"{self.user.name}'s affirmation: {self.text[:50]}..."


class GratitudeManager(AbstractManager):
    pass


class Gratitude(AbstractModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='gratitudes')
    text = models.TextField()
    is_active = models.BooleanField(default=True)
    order = models.PositiveIntegerField(default=0)
    
    objects = GratitudeManager()
    
    class Meta:
        ordering = ['order', 'created']
        unique_together = ['user', 'text']
    
    def __str__(self):
        return f"{self.user.name}'s gratitude: {self.text[:50]}..."


class PassionManager(AbstractManager):
    pass


class Passion(AbstractModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='passions')
    text = models.TextField()
    is_active = models.BooleanField(default=True)
    order = models.PositiveIntegerField(default=0)
    
    objects = PassionManager()
    
    class Meta:
        ordering = ['order', 'created']
        unique_together = ['user', 'text']
    
    def __str__(self):
        return f"{self.user.name}'s passion: {self.text[:50]}..."


class FavoriteThingManager(AbstractManager):
    pass


class FavoriteThing(AbstractModel):
    CATEGORY_CHOICES = [
        ('song', 'Song'),
        ('movie', 'Movie'),
        ('book', 'Book'),
        ('color', 'Color'),
        ('season', 'Season'),
        ('food', 'Food'),
        ('place', 'Place'),
        ('hobby', 'Hobby'),
        ('other', 'Other'),
    ]
    
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='favorite_things')
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    order = models.PositiveIntegerField(default=0)
    
    objects = FavoriteThingManager()
    
    class Meta:
        ordering = ['category', 'order', 'created']
        unique_together = ['user', 'category', 'title']
    
    def __str__(self):
        return f"{self.user.name}'s favorite {self.category}: {self.title}"


class AboutManager(AbstractManager):
    pass


class About(AbstractModel):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='about')
    
    # Personal Information
    nickname = models.CharField(max_length=100, blank=True, null=True)
    pronouns = models.CharField(max_length=50, blank=True, null=True)
    location = models.CharField(max_length=200, blank=True, null=True)
    occupation = models.CharField(max_length=200, blank=True, null=True)
    education = models.TextField(blank=True, null=True)
    
    # Personal Details
    personality_type = models.CharField(max_length=50, blank=True, null=True)  # MBTI, Enneagram, etc.
    zodiac_sign = models.CharField(max_length=50, blank=True, null=True)
    life_goals = models.TextField(blank=True, null=True)
    personal_mission = models.TextField(blank=True, null=True)
    
    # Interests & Lifestyle
    hobbies = models.TextField(blank=True, null=True)
    interests = models.TextField(blank=True, null=True)
    lifestyle_preferences = models.TextField(blank=True, null=True)  # Introvert/Extrovert, etc.
    
    # Personal Story
    personal_story = models.TextField(blank=True, null=True)
    achievements = models.TextField(blank=True, null=True)
    challenges_overcome = models.TextField(blank=True, null=True)
    
    # Values & Beliefs
    core_values = models.TextField(blank=True, null=True)
    beliefs = models.TextField(blank=True, null=True)
    philosophy = models.TextField(blank=True, null=True)
    
    # Social & Relationships
    relationship_status = models.CharField(max_length=100, blank=True, null=True)
    family_info = models.TextField(blank=True, null=True)
    social_preferences = models.TextField(blank=True, null=True)
    
    # Professional
    career_goals = models.TextField(blank=True, null=True)
    skills = models.TextField(blank=True, null=True)
    work_style = models.TextField(blank=True, null=True)
    
    # Health & Wellness
    health_goals = models.TextField(blank=True, null=True)
    fitness_preferences = models.TextField(blank=True, null=True)
    wellness_practices = models.TextField(blank=True, null=True)
    
    # Creative & Expression
    creative_interests = models.TextField(blank=True, null=True)
    artistic_preferences = models.TextField(blank=True, null=True)
    self_expression = models.TextField(blank=True, null=True)
    
    # Future & Dreams
    bucket_list = models.TextField(blank=True, null=True)
    dreams_aspirations = models.TextField(blank=True, null=True)
    future_plans = models.TextField(blank=True, null=True)
    
    # Additional Notes
    notes = models.TextField(blank=True, null=True)
    is_public = models.BooleanField(default=False)  # Whether to show in public profile
    
    objects = AboutManager()
    
    class Meta:
        verbose_name_plural = "About"
    
    def __str__(self):
        return f"{self.user.name}'s about section"
    
    def get_display_name(self):
        """Get the display name (nickname or full name)"""
        return self.nickname or self.user.name
    
    def get_summary(self):
        """Get a brief summary of the about section"""
        summary_parts = []
        if self.occupation:
            summary_parts.append(f"Works as {self.occupation}")
        if self.location:
            summary_parts.append(f"Lives in {self.location}")
        if self.personality_type:
            summary_parts.append(f"Personality: {self.personality_type}")
        if self.hobbies:
            summary_parts.append(f"Enjoys {self.hobbies[:50]}...")
        
        return " | ".join(summary_parts) if summary_parts else "No summary available"
