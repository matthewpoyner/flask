{% extends 'base.html' %} {% block content %}

<div class="row">
    <div class="col-md-5">
        <img src="{{ member.image_source }}" alt="Profile image for {{member.name}}" />
        <h2 class="col-md-7">{{ member.name }}</h2>
    </div>
</div>

<div class="col-md-12">
    <p>{{ member.description }}</p>
</div>

{% endblock %}