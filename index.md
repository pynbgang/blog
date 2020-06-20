---
layout: page
title: PYNB GANG
tagline: -- tech (programming, networking) tips 
---
{% include JB/setup %}

<!--
![image](https://user-images.githubusercontent.com/2038044/76429344-4a812800-6385-11ea-9353-6f8288aaa7dd.png)
-->

resources/tips/notes:

* [about strings](https://towardsdatascience.com/41-questions-to-test-your-knowledge-of-python-strings-9eb473aa8fe8)


<ul class="listing">
{% for post in site.posts %}

**topped posts**:

  {% if post.top == true %}

    {% capture y %}{{post.date | date:"%Y"}}{% endcapture %}
    {% if year != y %}
        {% assign year = y %}
        <li class="listing-seperator">{{ y }}</li>
    {% endif %}
    <li class="listing-item">
        <time datetime="{{ post.date | date:"%Y-%m-%d" }}">{{ post.date | date:"%Y-%m-%d" }}</time>
        <a href="{{ site.url }}{{ post.url }}" title="{{ post.title }}">{{ post.title }}</a>
    </li>

  {% endif %}

**all posts**:

  {% capture y %}{{post.date | date:"%Y"}}{% endcapture %}
  {% if year != y %}
    {% assign year = y %}
    <li class="listing-seperator">{{ y }}</li>
  {% endif %}
  <li class="listing-item">
    <time datetime="{{ post.date | date:"%Y-%m-%d" }}">{{ post.date | date:"%Y-%m-%d" }}</time>
    <a href="{{ site.url }}{{ post.url }}" title="{{ post.title }}">{{ post.title }}</a>
  </li>

{% endfor %}
</ul>

