from django import template
from django.utils.safestring import mark_safe
import markdown
from django.shortcuts import get_object_or_404

from ams.models import Billing
from ams.models import TenantProfile

register = template.Library()


#
# @register.simple_tag
# def total_posts():
#     return Post.published.count()
#
#
# @register.simple_tag
# def total_posts_pluralize():
#     s = ''
#     if Post.objects.count() > 1:
#         s = 's'
#     return s
#
#
# @register.inclusion_tag('blog/post/latest_posts.html')
# def show_latest_posts(count=5):
#     # latest_posts = Post.published.order_by('-publish')[:count]
#     latest_posts = Post.published.order_by('-publish')[:count]
#     return {'latest_posts': latest_posts}
#
#
# @register.simple_tag
# def get_most_commented_posts(count=5):
#     return Post.published.annotate(total_comments=Count('comments')).order_by('-total_comments')[:count]

@register.filter
# @register.filter(name='markdown')
def markdown_format(text):
    return mark_safe(markdown.markdown(text))


# @register.inclusion_tag('blog/post/latest_posts.html',name='show_latest_post_pb_test')
# def show_latest_posts_pb(count=5):
#     latest_posts = Post.published.order_by('-publish')[:count]
#     content = {'latest_posts':latest_posts}
#
#     return content

@register.inclusion_tag('ams/payment_tag.html')
def display_tenant_bill_data(rmno):
    tenant_bill = get_object_or_404(Billing, room_no=rmno, status='open')

    bill_misc = tenant_bill.late_fee + tenant_bill.maint_cost

    return {'tenant_bill': tenant_bill, 'bill_misc': bill_misc}


@register.inclusion_tag('ams/payment_individual_tag.html')
def display_individual_tenant_bill_data(rmno):
    tenant_bill = get_object_or_404(Billing, room_no=rmno, status='open')

    room_cost_acc = tenant_bill.room_cost + tenant_bill.room_acc_cost + tenant_bill.adjust

    bill_misc = tenant_bill.late_fee + tenant_bill.maint_cost

    return {'tenant_bill': tenant_bill, 'room_cost_acc': room_cost_acc,'bill_misc':bill_misc}


@register.simple_tag
def room_acc_cost(rmno):
    tenant_pf = get_object_or_404(TenantProfile, room_no__room_no=rmno)
    extra = tenant_pf.extra.all()

    exd = {}
    exd.setdefault('Electricity CPU', 0)
    exd.setdefault('Water CPU', 0)
    exd.setdefault('Garbage', 0)
    exd.setdefault('Parking', 0)
    exd.setdefault('Wifi', 0)
    exd.setdefault('Cable TV', 0)
    exd.setdefault('Bed', 0)
    exd.setdefault('Bed accessories', 0)
    exd.setdefault('Dressing Table', 0)
    exd.setdefault('Clothing Cupboard', 0)
    exd.setdefault('TV Table', 0)
    exd.setdefault('Fridge', 0)
    exd.setdefault('Air-Conditioner', 0)

    for e in extra:
        exd.update({e.desc: e.cpu})

    room_acc_cost = exd['Bed'] + exd['Bed accessories'] + exd['Dressing Table'] \
                    + exd['Clothing Cupboard'] + exd['TV Table'] + exd['Fridge'] \
                    + exd['Air-Conditioner']

    return '{0:3,.0f}'.format(room_acc_cost)


@register.simple_tag
def room_other_cost(rmno):
    tenant_pf = get_object_or_404(TenantProfile, room_no__room_no=rmno)
    extra = tenant_pf.extra.all()

    exd = {}
    exd.setdefault('Electricity CPU', 0)
    exd.setdefault('Water CPU', 0)
    exd.setdefault('Garbage', 0)
    exd.setdefault('Parking', 0)
    exd.setdefault('Wifi', 0)
    exd.setdefault('Cable TV', 0)
    exd.setdefault('Bed', 0)
    exd.setdefault('Bed accessories', 0)
    exd.setdefault('Dressing Table', 0)
    exd.setdefault('Clothing Cupboard', 0)
    exd.setdefault('TV Table', 0)
    exd.setdefault('Fridge', 0)
    exd.setdefault('Air-Conditioner', 0)

    for e in extra:
        exd.update({e.desc: e.cpu})

    oth_ser_cost = exd['Garbage'] + exd['Parking'] + exd['Wifi'] + exd['Cable TV']

    return '{0:>3,.0f}'.format(oth_ser_cost)
