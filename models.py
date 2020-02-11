# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Achievements(models.Model):
    group_name = models.CharField(max_length=64)
    category = models.CharField(max_length=25)
    level = models.IntegerField()
    reward_pixels = models.IntegerField()
    reward_points = models.IntegerField()
    progress_needed = models.IntegerField()
    game_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'achievements'


class AchievementsTalents(models.Model):
    type = models.CharField(max_length=11)
    parent_category = models.IntegerField()
    level = models.IntegerField()
    order_num = models.IntegerField()
    achievement_group = models.CharField(max_length=255)
    achievement_level = models.IntegerField()
    prize = models.CharField(max_length=255)
    prize_baseitem = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'achievements_talents'


class BadgeDefinitions(models.Model):
    code = models.CharField(primary_key=True, max_length=35)
    required_right = models.CharField(max_length=25)

    class Meta:
        managed = False
        db_table = 'badge_definitions'


class BadgeShop(models.Model):
    badge_id = models.CharField(max_length=10)
    cost = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'badge_shop'


class BadgesBuys(models.Model):
    badge_id = models.CharField(max_length=255)
    user_id = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'badges_buys'


class Bans(models.Model):
    bantype = models.CharField(max_length=7)
    value = models.CharField(max_length=50)
    reason = models.TextField()
    expire = models.FloatField()
    added_by = models.CharField(max_length=50)
    added_date = models.CharField(max_length=50)
    appeal_state = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'bans'


class BansAppeals(models.Model):
    ban_id = models.IntegerField()
    send_ip = models.CharField(max_length=50)
    send_date = models.CharField(max_length=120)
    mail = models.CharField(max_length=120)
    plea = models.TextField()

    class Meta:
        managed = False
        db_table = 'bans_appeals'


class Bots(models.Model):
    room_id = models.PositiveIntegerField()
    user_id = models.PositiveIntegerField()
    ai_type = models.CharField(max_length=9)
    name = models.CharField(max_length=100)
    motto = models.CharField(max_length=120)
    look = models.TextField()
    x = models.IntegerField()
    y = models.IntegerField()
    z = models.IntegerField()
    rotation = models.IntegerField()
    walk_mode = models.CharField(max_length=15)
    min_x = models.IntegerField()
    min_y = models.IntegerField()
    max_x = models.IntegerField()
    max_y = models.IntegerField()
    effect = models.IntegerField()
    gender = models.CharField(max_length=5)
    dance = models.IntegerField()
    automatic_chat = models.CharField(max_length=5)
    speaking_interval = models.IntegerField()
    mix_sentences = models.CharField(max_length=1)
    chat_bubble = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'bots'


class BotsPetCommands(models.Model):
    input_title = models.CharField(max_length=255)
    input = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bots_pet_commands'


class BotsPetResponses(models.Model):
    pet_id = models.CharField(primary_key=True, max_length=255)
    responses = models.TextField()

    class Meta:
        managed = False
        db_table = 'bots_pet_responses'


class BotsPetdata(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    type = models.PositiveIntegerField(blank=True, null=True)
    race = models.CharField(max_length=11, blank=True, null=True)
    color = models.CharField(max_length=11, blank=True, null=True)
    energy = models.IntegerField(blank=True, null=True)
    experience = models.IntegerField(blank=True, null=True)
    nutrition = models.IntegerField(blank=True, null=True)
    respect = models.IntegerField(blank=True, null=True)
    createstamp = models.IntegerField(blank=True, null=True)
    have_saddle = models.IntegerField(blank=True, null=True)
    hairdye = models.IntegerField(blank=True, null=True)
    pethair = models.IntegerField(blank=True, null=True)
    anyone_ride = models.IntegerField(blank=True, null=True)
    gnome_clothing = models.CharField(max_length=85, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bots_petdata'


class BotsResponses(models.Model):
    bot_ai = models.CharField(max_length=9)
    chat_keywords = models.TextField()
    response_text = models.CharField(max_length=200)
    response_mode = models.CharField(max_length=7)
    response_beverage = models.CharField(max_length=25)

    class Meta:
        managed = False
        db_table = 'bots_responses'


class BotsSpeech(models.Model):
    bot_id = models.PositiveIntegerField()
    text = models.CharField(max_length=200)
    shout = models.CharField(max_length=1)
    type = models.CharField(max_length=8, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bots_speech'


class BugReports(models.Model):
    type = models.CharField(max_length=50)
    user = models.CharField(max_length=50)
    message = models.CharField(max_length=500)
    status = models.CharField(max_length=1)
    staff = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bug_reports'


class CameraPhotos(models.Model):
    creator_id = models.IntegerField()
    creator_name = models.CharField(max_length=50)
    file_state = models.CharField(max_length=9)
    file_name = models.CharField(max_length=50)
    reports = models.IntegerField()
    deleted = models.CharField(max_length=1)
    ip_address = models.CharField(max_length=50)
    created_at = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'camera_photos'


class CatalogBotPresets(models.Model):
    name = models.CharField(max_length=255)
    figure = models.CharField(max_length=255)
    gender = models.CharField(max_length=255)
    motto = models.CharField(max_length=255)
    ai_type = models.CharField(max_length=9)

    class Meta:
        managed = False
        db_table = 'catalog_bot_presets'


class CatalogClothing(models.Model):
    clothing_name = models.CharField(max_length=55)
    clothing_parts = models.CharField(max_length=85)

    class Meta:
        managed = False
        db_table = 'catalog_clothing'


class CatalogDeals(models.Model):
    page_id = models.IntegerField()
    items = models.TextField()
    name = models.CharField(max_length=35)
    cost_credits = models.IntegerField()
    cost_pixels = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'catalog_deals'


class CatalogItems(models.Model):
    page_id = models.IntegerField()
    item_id = models.CharField(max_length=120)
    catalog_name = models.CharField(max_length=100)
    cost_credits = models.IntegerField()
    cost_pixels = models.IntegerField()
    cost_diamonds = models.IntegerField()
    amount = models.IntegerField()
    limited_sells = models.IntegerField()
    limited_stack = models.IntegerField()
    offer_active = models.CharField(max_length=1)
    extradata = models.CharField(max_length=255)
    badge = models.CharField(max_length=5)
    offer_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'catalog_items'


class CatalogMarketplaceData(models.Model):
    sprite = models.IntegerField()
    sold = models.IntegerField()
    avgprice = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'catalog_marketplace_data'


class CatalogMarketplaceOffers(models.Model):
    offer_id = models.AutoField(primary_key=True)
    item_id = models.PositiveIntegerField()
    user_id = models.PositiveIntegerField()
    asking_price = models.IntegerField()
    total_price = models.IntegerField()
    public_name = models.TextField()
    sprite_id = models.IntegerField()
    item_type = models.CharField(max_length=1)
    timestamp = models.FloatField()
    state = models.CharField(max_length=1)
    extra_data = models.TextField()
    furni_id = models.PositiveIntegerField()
    limited_number = models.IntegerField()
    limited_stack = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'catalog_marketplace_offers'


class CatalogPages(models.Model):
    parent_id = models.IntegerField()
    caption = models.CharField(max_length=35)
    icon_image = models.IntegerField()
    visible = models.CharField(max_length=1)
    enabled = models.CharField(max_length=1)
    min_rank = models.PositiveIntegerField()
    min_vip = models.IntegerField()
    order_num = models.IntegerField()
    page_link = models.CharField(max_length=35)
    page_layout = models.CharField(max_length=35)
    page_strings_1 = models.TextField()
    page_strings_2 = models.TextField()

    class Meta:
        managed = False
        db_table = 'catalog_pages'


class CatalogPetRaces(models.Model):
    raceid = models.IntegerField(blank=True, null=True)
    color1 = models.IntegerField(blank=True, null=True)
    color2 = models.IntegerField(blank=True, null=True)
    has1color = models.CharField(max_length=1, blank=True, null=True)
    has2color = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'catalog_pet_races'


class CatalogVouchers(models.Model):
    voucher = models.CharField(primary_key=True, max_length=45)
    type = models.CharField(max_length=7)
    value = models.IntegerField()
    current_uses = models.IntegerField()
    max_uses = models.IntegerField()
    enabled = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'catalog_vouchers'


class Changelogs(models.Model):
    id = models.AutoField(unique=True)
    poster_id = models.IntegerField()
    message = models.CharField(max_length=250)
    posted_on = models.CharField(max_length=300)

    class Meta:
        managed = False
        db_table = 'changelogs'


class Chatlogs(models.Model):
    user_id = models.PositiveIntegerField()
    room_id = models.PositiveIntegerField()
    message = models.TextField()
    timestamp = models.FloatField()

    class Meta:
        managed = False
        db_table = 'chatlogs'


class ChatlogsConsole(models.Model):
    from_id = models.PositiveIntegerField()
    to_id = models.PositiveIntegerField()
    message = models.TextField()
    timestamp = models.FloatField()

    class Meta:
        managed = False
        db_table = 'chatlogs_console'


class ChatlogsConsoleInvitations(models.Model):
    user_id = models.IntegerField()
    message = models.TextField()
    timestamp = models.FloatField()

    class Meta:
        managed = False
        db_table = 'chatlogs_console_invitations'


class ClientExternalBadgeTexts(models.Model):
    badge_code = models.CharField(max_length=35)
    badge_title = models.CharField(max_length=75)
    badge_desc = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'client_external_badge_texts'


class ClientExternalTexts(models.Model):
    key = models.CharField(max_length=70)
    value = models.TextField()

    class Meta:
        managed = False
        db_table = 'client_external_texts'


class CmsAlerts(models.Model):
    userid = models.IntegerField()
    alert = models.TextField()

    class Meta:
        managed = False
        db_table = 'cms_alerts'


class CmsBadges(models.Model):
    code = models.CharField(max_length=40, blank=True, null=True)
    price = models.CharField(max_length=40, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cms_badges'


class CmsBadgesGift(models.Model):
    code = models.CharField(max_length=40, blank=True, null=True)
    price = models.CharField(max_length=40, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cms_badges_gift'


class CmsBadgesReg(models.Model):
    id = models.IntegerField()
    code = models.CharField(max_length=40, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cms_badges_reg'


class CmsCampaigns(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    shortstory = models.TextField(blank=True, null=True)
    image = models.CharField(max_length=255, blank=True, null=True)
    author = models.TextField(blank=True, null=True)
    time = models.FloatField()
    link = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'cms_campaigns'


class CmsComments(models.Model):
    username = models.CharField(max_length=50)
    comentario = models.TextField()
    posted_on = models.DateField()
    posted_in = models.IntegerField()
    type = models.CharField(max_length=8)
    time = models.IntegerField()
    aus = models.CharField(max_length=20, blank=True, null=True)
    backaus = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cms_comments'


class CmsForumPosts(models.Model):
    threadid = models.IntegerField()
    message = models.TextField()
    author = models.CharField(max_length=25)
    date = models.CharField(max_length=30)
    edit_date = models.CharField(max_length=30)
    edit_author = models.CharField(max_length=25)
    forumid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cms_forum_posts'


class CmsForumThreads(models.Model):
    type = models.IntegerField()
    title = models.CharField(max_length=30)
    author = models.CharField(max_length=25)
    date = models.CharField(max_length=35)
    lastpost_author = models.CharField(max_length=25)
    lastpost_date = models.CharField(max_length=35)
    views = models.IntegerField()
    posts = models.IntegerField()
    unix = models.CharField(max_length=40)
    forumid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cms_forum_threads'


class CmsHotcampaigns(models.Model):
    image_url = models.TextField()
    caption = models.TextField()
    descr = models.TextField()
    url = models.TextField()

    class Meta:
        managed = False
        db_table = 'cms_hotcampaigns'


class CmsJogosorte(models.Model):
    num_esc1 = models.IntegerField()
    num_esc2 = models.IntegerField()
    num_sort1 = models.IntegerField()
    num_sort2 = models.IntegerField()
    user = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'cms_jogosorte'


class CmsMarktplatz(models.Model):
    image = models.CharField(max_length=255)
    name = models.CharField(max_length=255, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    credits = models.IntegerField()
    pixels = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cms_marktplatz'


class CmsMinimail(models.Model):
    sender_id = models.PositiveIntegerField()
    receiver_id = models.PositiveIntegerField()
    folder = models.CharField(max_length=5)
    is_read = models.CharField(max_length=1)
    subject = models.CharField(max_length=120)
    date = models.CharField(max_length=120)
    isodate = models.CharField(max_length=120)
    timestamp = models.IntegerField()
    body = models.TextField()
    conversationid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cms_minimail'


class CmsNavi(models.Model):
    name = models.CharField(max_length=20)
    zone = models.CharField(max_length=50)
    tab = models.IntegerField(db_column='TAB')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cms_navi'


class CmsNews(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    shortstory = models.TextField(blank=True, null=True)
    longstory = models.TextField(blank=True, null=True)
    published = models.IntegerField()
    image = models.CharField(max_length=255, blank=True, null=True)
    campaign = models.IntegerField()
    campaignimg = models.CharField(max_length=255)
    author = models.CharField(max_length=100)
    big_image = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'cms_news'


class CmsNewsSlider(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    shortstory = models.TextField(blank=True, null=True)
    image = models.CharField(max_length=255, blank=True, null=True)
    botaotexto = models.CharField(max_length=15)
    linkbotao = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'cms_news_slider'


class CmsRares(models.Model):
    code = models.CharField(max_length=40, blank=True, null=True)
    price = models.CharField(max_length=40, blank=True, null=True)
    item_name = models.CharField(max_length=40)

    class Meta:
        managed = False
        db_table = 'cms_rares'


class CmsRecommended(models.Model):
    id_rec = models.IntegerField(blank=True, null=True)
    type = models.CharField(max_length=5)

    class Meta:
        managed = False
        db_table = 'cms_recommended'


class CmsSettings(models.Model):
    variable = models.CharField(primary_key=True, max_length=80)
    value = models.TextField()
    description = models.TextField(blank=True, null=True)
    example = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cms_settings'


class CmsSlider(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    image = models.CharField(max_length=255, blank=True, null=True)
    story = models.TextField(blank=True, null=True)
    longstory = models.TextField(blank=True, null=True)
    author = models.TextField(blank=True, null=True)
    time = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cms_slider'


class CmsTransactions(models.Model):
    date = models.CharField(max_length=20)
    amount = models.CharField(max_length=10)
    descr = models.TextField()
    userid = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cms_transactions'


class Comments(models.Model):
    name = models.CharField(max_length=40)
    email = models.CharField(max_length=60)
    comment = models.TextField()
    id_post = models.IntegerField()
    date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'comments'


class CreditVouchers(models.Model):
    code = models.CharField(max_length=50)
    value = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'credit_vouchers'


class Faq(models.Model):
    question = models.TextField()
    answer = models.TextField()

    class Meta:
        managed = False
        db_table = 'faq'


class Furniture(models.Model):
    item_name = models.CharField(max_length=70)
    public_name = models.CharField(max_length=56)
    type = models.CharField(max_length=1)
    width = models.IntegerField()
    length = models.IntegerField()
    stack_height = models.FloatField()
    can_stack = models.CharField(max_length=1)
    can_sit = models.CharField(max_length=1)
    is_walkable = models.CharField(max_length=1)
    sprite_id = models.IntegerField()
    allow_recycle = models.CharField(max_length=1)
    allow_trade = models.CharField(max_length=1)
    allow_marketplace_sell = models.CharField(max_length=1)
    allow_gift = models.CharField(max_length=1)
    allow_inventory_stack = models.CharField(max_length=1)
    interaction_type = models.CharField(max_length=25)
    interaction_modes_count = models.IntegerField()
    vending_ids = models.CharField(max_length=255)
    height_adjustable = models.CharField(max_length=50)
    effect_id = models.IntegerField()
    wired_id = models.IntegerField()
    is_rare = models.CharField(max_length=1)
    clothing_id = models.IntegerField()
    extra_rot = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'furniture'


class FurnitureMusic(models.Model):
    name = models.CharField(max_length=255)
    title = models.CharField(max_length=64)
    artist = models.CharField(max_length=32)
    song_data = models.TextField()
    length = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'furniture_music'


class GamesConfig(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=25)
    colour_one = models.CharField(max_length=25)
    colour_two = models.CharField(max_length=25)
    resource_path = models.CharField(max_length=125)
    string_three = models.CharField(max_length=25)
    game_swf = models.CharField(max_length=255)
    game_assets = models.CharField(max_length=255)
    game_server_host = models.CharField(max_length=25)
    game_server_port = models.CharField(max_length=25)
    socket_policy_port = models.CharField(max_length=25)
    game_enabled = models.CharField(max_length=1, blank=True, null=True)
    last_reset = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'games_config'


class GamesFastfoodObjects(models.Model):
    objectname = models.CharField(db_column='ObjectName', primary_key=True, max_length=25)  # Field name made lowercase.
    objecttype = models.CharField(db_column='ObjectType', max_length=12)  # Field name made lowercase.
    objectprice = models.IntegerField(db_column='ObjectPrice')  # Field name made lowercase.
    objectbundle = models.IntegerField(db_column='ObjectBundle')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'games_fastfood_objects'


class GamesFastfoodPlates(models.Model):
    plateid = models.IntegerField(db_column='PlateId', primary_key=True)  # Field name made lowercase.
    platesomething = models.CharField(db_column='PlateSomething', max_length=10, blank=True, null=True)  # Field name made lowercase.
    platedropspeed = models.CharField(db_column='PlateDropSpeed', max_length=8)  # Field name made lowercase.
    plateparachutespeed = models.CharField(db_column='PlateParachuteSpeed', max_length=8)  # Field name made lowercase.
    platebigparachutespeed = models.CharField(db_column='PlateBigParachuteSpeed', max_length=8)  # Field name made lowercase.
    platepreptime = models.IntegerField(db_column='PlatePrepTime')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'games_fastfood_plates'


class Granasocial(models.Model):
    link = models.TextField()
    status = models.CharField(max_length=7)

    class Meta:
        managed = False
        db_table = 'granasocial'


class GranasocialView(models.Model):
    id_anuncio = models.CharField(max_length=255)
    usuario = models.CharField(max_length=255)
    ip = models.CharField(max_length=255)
    data = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'granasocial_view'


class GroupForumsSettings(models.Model):
    group_id = models.IntegerField(primary_key=True)
    who_can_read = models.IntegerField()
    who_can_post = models.IntegerField()
    who_can_init_discussions = models.IntegerField()
    who_can_mod = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'group_forums_settings'


class GroupForumsThreadPosts(models.Model):
    thread_id = models.IntegerField()
    user_id = models.IntegerField()
    message = models.TextField()
    timestamp = models.IntegerField()
    deleted_level = models.IntegerField()
    deleter_user_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'group_forums_thread_posts'


class GroupForumsThreadViews(models.Model):
    thread_id = models.IntegerField()
    user_id = models.IntegerField()
    count = models.IntegerField()
    timestamp = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'group_forums_thread_views'


class GroupForumsThreads(models.Model):
    forum_id = models.IntegerField()
    user_id = models.IntegerField()
    caption = models.TextField()
    pinned = models.IntegerField()
    locked = models.IntegerField()
    deleted_level = models.IntegerField()
    deleter_user_id = models.IntegerField()
    timestamp = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'group_forums_threads'


class GroupForumsThreadsViews(models.Model):
    forum_id = models.IntegerField()
    user_id = models.IntegerField()
    caption = models.TextField()
    pinned = models.IntegerField()
    locked = models.IntegerField()
    deleted_level = models.IntegerField()
    deleter_user_id = models.IntegerField()
    timestamp = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'group_forums_threads_views'


class GroupMemberships(models.Model):
    group_id = models.PositiveIntegerField()
    user_id = models.PositiveIntegerField()
    rank = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'group_memberships'


class GroupRequests(models.Model):
    group_id = models.PositiveIntegerField()
    user_id = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'group_requests'


class Groups(models.Model):
    name = models.CharField(max_length=50)
    desc = models.CharField(max_length=255)
    badge = models.CharField(max_length=50)
    owner_id = models.PositiveIntegerField()
    created = models.IntegerField()
    room_id = models.PositiveIntegerField()
    state = models.CharField(max_length=1)
    colour1 = models.IntegerField()
    colour2 = models.IntegerField()
    admindeco = models.CharField(max_length=1, blank=True, null=True)
    has_forum = models.CharField(max_length=1)
    forum_name = models.CharField(max_length=255)
    forum_description = models.CharField(max_length=4096)
    forum_messages_count = models.PositiveIntegerField()
    forum_score = models.CharField(max_length=255)
    forum_lastposter_id = models.PositiveIntegerField()
    forum_lastposter_name = models.CharField(max_length=255)
    forum_lastposter_timestamp = models.IntegerField()
    who_can_read = models.IntegerField()
    who_can_post = models.IntegerField()
    who_can_thread = models.IntegerField()
    who_can_mod = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'groups'


class GroupsItems(models.Model):
    type = models.CharField(max_length=6)
    id = models.IntegerField(primary_key=True)
    firstvalue = models.CharField(max_length=255)
    secondvalue = models.CharField(max_length=2000)
    enabled = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'groups_items'
        unique_together = (('id', 'type'),)


class HeliocmsAvatars(models.Model):
    user_id = models.IntegerField()
    parent_email = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'heliocms_avatars'


class HeliocmsBadgestore(models.Model):
    price = models.CharField(max_length=30)
    code = models.CharField(max_length=40)

    class Meta:
        managed = False
        db_table = 'heliocms_badgestore'


class HeliocmsForgotten(models.Model):
    email = models.CharField(max_length=500)

    class Meta:
        managed = False
        db_table = 'heliocms_forgotten'


class HeliocmsHotel(models.Model):
    host = models.CharField(max_length=5000)
    port = models.CharField(max_length=5000)
    external_variables = models.CharField(max_length=5000)
    external_flash_texts = models.CharField(max_length=5000)
    external_flash_override_texts = models.CharField(max_length=5000)
    external_override_variables = models.CharField(max_length=5000)
    furnidata = models.CharField(max_length=5000)
    figuredata = models.CharField(max_length=5000)
    base = models.CharField(max_length=5000)
    habbo_swf = models.CharField(max_length=5000)
    sitename = models.CharField(max_length=5000)
    site = models.CharField(max_length=500)
    aka = models.CharField(max_length=500)
    productdata = models.CharField(max_length=500)
    avatarimage = models.CharField(max_length=500)

    class Meta:
        managed = False
        db_table = 'heliocms_hotel'


class HeliocmsNews(models.Model):
    title = models.CharField(max_length=5000)
    category = models.CharField(max_length=13)
    image_url = models.CharField(max_length=5000)
    time = models.CharField(max_length=5000)
    stext = models.CharField(max_length=5000)
    btext = models.TextField()
    kind = models.CharField(max_length=1)
    image_url_thumb = models.CharField(max_length=5000)

    class Meta:
        managed = False
        db_table = 'heliocms_news'


class HeliocmsNewsCategories(models.Model):
    name = models.CharField(max_length=500)
    code = models.CharField(max_length=500)

    class Meta:
        managed = False
        db_table = 'heliocms_news_categories'


class HeliocmsProfilesettings(models.Model):
    profile_visible = models.CharField(max_length=1)
    email = models.CharField(max_length=500)
    safety_questions = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'heliocms_profilesettings'


class HeliocmsSafetyquestions(models.Model):
    email = models.CharField(max_length=500)
    trusted_ip = models.CharField(max_length=500)
    active = models.CharField(max_length=1)
    question1 = models.CharField(max_length=500)
    answer1 = models.CharField(max_length=500)
    question2 = models.CharField(max_length=500)
    answer2 = models.CharField(max_length=500)

    class Meta:
        managed = False
        db_table = 'heliocms_safetyquestions'


class HeliocmsSafetyquestionsDatabase(models.Model):
    id = models.IntegerField()
    question = models.CharField(max_length=500)
    code = models.CharField(max_length=500)

    class Meta:
        managed = False
        db_table = 'heliocms_safetyquestions_database'


class HeliocmsSessions(models.Model):
    last = models.CharField(max_length=50)
    user_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'heliocms_sessions'


class HomesStickers(models.Model):
    userid = models.IntegerField()
    x = models.CharField(max_length=6)
    y = models.CharField(max_length=6)
    z = models.CharField(max_length=6)
    data = models.TextField()
    type = models.CharField(max_length=1)
    subtype = models.CharField(max_length=1)
    skin = models.TextField()
    groupid = models.IntegerField()
    var = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'homes_stickers'


class Items(models.Model):
    user_id = models.IntegerField()
    room_id = models.PositiveIntegerField()
    base_item = models.PositiveIntegerField()
    extra_data = models.TextField()
    x = models.IntegerField()
    y = models.IntegerField()
    z = models.FloatField()
    rot = models.IntegerField()
    wall_pos = models.CharField(max_length=100, blank=True, null=True)
    limited_number = models.IntegerField(blank=True, null=True)
    limited_stack = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'items'


class ItemsGroups(models.Model):
    group_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'items_groups'


class ItemsYoutube(models.Model):
    youtube_id = models.CharField(max_length=35)
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=150)
    enabled = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'items_youtube'


class LogClient(models.Model):
    user = models.CharField(max_length=50)
    ip = models.CharField(db_column='IP', max_length=50)  # Field name made lowercase.
    correto = models.CharField(max_length=50)
    tentativas = models.CharField(max_length=50)
    expire = models.CharField(max_length=50)
    date = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'log_client'


class LogsClientNamechange(models.Model):
    user_id = models.IntegerField()
    new_name = models.CharField(max_length=50)
    old_name = models.CharField(max_length=50)
    timestamp = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'logs_client_namechange'


class LogsClientStaff(models.Model):
    user_id = models.IntegerField()
    data_string = models.TextField()
    machine_id = models.CharField(max_length=75)
    timestamp = models.FloatField()

    class Meta:
        managed = False
        db_table = 'logs_client_staff'


class LogsClientTrade(models.Model):
    number_1id = models.IntegerField(db_column='1id', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_2id = models.IntegerField(db_column='2id', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_1items = models.TextField(db_column='1items', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_2items = models.TextField(db_column='2items', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    timestamp = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'logs_client_trade'


class LogsVisitedhomes(models.Model):
    id = models.AutoField(unique=True)
    id_user = models.IntegerField()
    id_target = models.IntegerField()
    timestamp = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'logs_visitedhomes'


class LotteryTickets(models.Model):
    username = models.CharField(primary_key=True, max_length=50)
    ticket_number = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'lottery_tickets'


class Lotterycontrols(models.Model):
    id = models.IntegerField(primary_key=True)
    firstrare = models.TextField(db_column='FirstRare')  # Field name made lowercase.
    secondrare = models.TextField(db_column='SecondRare')  # Field name made lowercase.
    thirdrare = models.TextField(db_column='ThirdRare')  # Field name made lowercase.
    fourthrare = models.TextField(db_column='FourthRare')  # Field name made lowercase.
    startprize = models.TextField(db_column='StartPrize')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'lotterycontrols'


class MessengerFriendships(models.Model):
    user_one_id = models.PositiveIntegerField()
    user_two_id = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'messenger_friendships'


class MessengerOfflineMessages(models.Model):
    to_id = models.PositiveIntegerField()
    from_id = models.PositiveIntegerField()
    message = models.CharField(max_length=255)
    timestamp = models.FloatField()

    class Meta:
        managed = False
        db_table = 'messenger_offline_messages'


class MessengerRequests(models.Model):
    from_id = models.PositiveIntegerField()
    to_id = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'messenger_requests'


class ModerationPresetActionCategories(models.Model):
    caption = models.CharField(max_length=32)

    class Meta:
        managed = False
        db_table = 'moderation_preset_action_categories'


class ModerationPresetActionMessages(models.Model):
    parent_id = models.PositiveIntegerField()
    caption = models.CharField(max_length=32)
    message_text = models.TextField()
    mute_hours = models.IntegerField()
    ban_hours = models.IntegerField()
    ip_ban_hours = models.IntegerField()
    trade_lock_days = models.IntegerField()
    notice = models.TextField()

    class Meta:
        managed = False
        db_table = 'moderation_preset_action_messages'


class ModerationPresets(models.Model):
    type = models.CharField(max_length=4)
    message = models.TextField()
    enabled = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'moderation_presets'


class ModerationTickets(models.Model):
    score = models.IntegerField()
    type = models.IntegerField()
    status = models.CharField(max_length=8)
    sender_id = models.PositiveIntegerField()
    reported_id = models.PositiveIntegerField()
    moderator_id = models.PositiveIntegerField()
    message = models.TextField()
    room_id = models.PositiveIntegerField()
    room_name = models.CharField(max_length=100)
    timestamp = models.FloatField()

    class Meta:
        managed = False
        db_table = 'moderation_tickets'


class NavigatorCategories(models.Model):
    id = models.IntegerField(primary_key=True)
    category = models.CharField(max_length=13)
    category_identifier = models.CharField(max_length=35)
    public_name = models.CharField(max_length=35)
    view_mode = models.CharField(max_length=9)
    required_rank = models.IntegerField()
    category_type = models.CharField(max_length=25)
    search_allowance = models.CharField(max_length=9)
    enabled = models.CharField(max_length=1)
    order_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'navigator_categories'


class NavigatorPublics(models.Model):
    room_id = models.AutoField(primary_key=True)
    caption = models.CharField(max_length=64)
    description = models.CharField(max_length=150)
    image_url = models.TextField()
    order_num = models.IntegerField()
    enabled = models.CharField(max_length=1)
    category_type = models.CharField(max_length=25, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'navigator_publics'


class Permissions(models.Model):
    permission = models.CharField(max_length=50)
    description = models.TextField()

    class Meta:
        managed = False
        db_table = 'permissions'


class PermissionsCommands(models.Model):
    command = models.CharField(primary_key=True, max_length=45)
    group_id = models.IntegerField()
    subscription_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'permissions_commands'


class PermissionsGroups(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    badge_code = models.CharField(max_length=12)

    class Meta:
        managed = False
        db_table = 'permissions_groups'


class PermissionsRights(models.Model):
    group_id = models.IntegerField()
    permission_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'permissions_rights'


class PermissionsSubscriptions(models.Model):
    subscription_id = models.IntegerField()
    permission_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'permissions_subscriptions'


class ProfileWall(models.Model):
    id = models.AutoField(unique=True)
    page_id = models.IntegerField()
    poster_id = models.IntegerField()
    message = models.CharField(max_length=250)
    posted_on = models.CharField(max_length=300)

    class Meta:
        managed = False
        db_table = 'profile_wall'


class Quests(models.Model):
    type = models.CharField(max_length=32)
    level_num = models.IntegerField()
    goal_type = models.IntegerField()
    goal_data = models.PositiveIntegerField()
    action = models.CharField(max_length=32)
    pixel_reward = models.IntegerField()
    data_bit = models.CharField(max_length=2)
    reward_type = models.CharField(max_length=1)
    timestamp_unlock = models.IntegerField()
    timestamp_lock = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'quests'


class Rankcampanha(models.Model):
    nome = models.CharField(max_length=255)
    pontos = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'rankcampanha'


class Rankevento(models.Model):
    nome = models.CharField(max_length=255)
    pontos = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'rankevento'


class Ranks(models.Model):
    name = models.CharField(max_length=50)
    badgeid = models.CharField(max_length=5)
    title = models.CharField(max_length=50)
    tab_colour = models.CharField(max_length=14)

    class Meta:
        managed = False
        db_table = 'ranks'


class RoomBans(models.Model):
    user_id = models.PositiveIntegerField(primary_key=True)
    room_id = models.PositiveIntegerField()
    expire = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'room_bans'
        unique_together = (('user_id', 'room_id'),)


class RoomChatStyles(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=25, blank=True, null=True)
    required_right = models.CharField(max_length=25, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'room_chat_styles'


class RoomFilter(models.Model):
    word = models.CharField(max_length=15)
    room_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'room_filter'


class RoomItemsMoodlight(models.Model):
    item_id = models.PositiveIntegerField()
    enabled = models.CharField(max_length=1)
    current_preset = models.IntegerField()
    preset_one = models.TextField()
    preset_two = models.TextField()
    preset_three = models.TextField()

    class Meta:
        managed = False
        db_table = 'room_items_moodlight'


class RoomItemsTeleLinks(models.Model):
    tele_one_id = models.PositiveIntegerField()
    tele_two_id = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'room_items_tele_links'


class RoomItemsToner(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    enabled = models.CharField(max_length=1, blank=True, null=True)
    data1 = models.IntegerField()
    data2 = models.IntegerField()
    data3 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'room_items_toner'


class RoomModels(models.Model):
    id = models.CharField(primary_key=True, max_length=100)
    door_x = models.IntegerField()
    door_y = models.IntegerField()
    door_z = models.FloatField()
    door_dir = models.IntegerField()
    heightmap = models.TextField()
    public_items = models.TextField()
    club_only = models.CharField(max_length=1)
    poolmap = models.CharField(max_length=100)
    custom = models.CharField(max_length=1)
    wall_height = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'room_models'


class RoomPromotions(models.Model):
    room_id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=35)
    description = models.CharField(max_length=220)
    timestamp_start = models.FloatField()
    timestamp_expire = models.FloatField()
    category_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'room_promotions'


class RoomRights(models.Model):
    room_id = models.PositiveIntegerField()
    user_id = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'room_rights'


class Rooms(models.Model):
    roomtype = models.CharField(max_length=7)
    caption = models.CharField(max_length=100)
    owner = models.CharField(max_length=75)
    description = models.CharField(max_length=255)
    category = models.IntegerField()
    state = models.CharField(max_length=9)
    users_now = models.IntegerField()
    users_max = models.IntegerField()
    model_name = models.CharField(max_length=50)
    score = models.IntegerField()
    tags = models.CharField(max_length=100)
    password = models.CharField(max_length=30)
    wallpaper = models.CharField(max_length=10)
    floor = models.CharField(max_length=10)
    landscape = models.CharField(max_length=10)
    allow_pets = models.CharField(max_length=1)
    allow_pets_eat = models.CharField(max_length=1)
    room_blocking_disabled = models.CharField(max_length=1)
    allow_hidewall = models.CharField(max_length=1)
    wallthick = models.IntegerField()
    floorthick = models.IntegerField()
    group_id = models.PositiveIntegerField()
    mute_settings = models.CharField(max_length=1)
    ban_settings = models.CharField(max_length=1)
    kick_settings = models.CharField(max_length=1)
    chat_mode = models.IntegerField()
    chat_size = models.IntegerField()
    chat_speed = models.IntegerField()
    chat_extra_flood = models.IntegerField()
    chat_hearing_distance = models.IntegerField()
    trade_settings = models.IntegerField()
    push_enabled = models.CharField(max_length=1)
    pull_enabled = models.CharField(max_length=1)
    enables_enabled = models.CharField(max_length=1)
    respect_notifications_enabled = models.CharField(max_length=1)
    pet_morphs_allowed = models.CharField(max_length=1)
    spull_enabled = models.CharField(max_length=1)
    spush_enabled = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'rooms'


class ServerLanding(models.Model):
    title = models.CharField(max_length=35, blank=True, null=True)
    text = models.TextField(blank=True, null=True)
    button_text = models.CharField(max_length=25, blank=True, null=True)
    button_type = models.CharField(max_length=1, blank=True, null=True)
    button_link = models.CharField(max_length=90, blank=True, null=True)
    image_link = models.CharField(max_length=120, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'server_landing'


class ServerLocale(models.Model):
    key = models.CharField(primary_key=True, max_length=255)
    value = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'server_locale'


class ServerPictures(models.Model):
    user_id = models.IntegerField()
    timestamp = models.CharField(max_length=255)
    url = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'server_pictures'


class ServerPicturesPublish(models.Model):
    picture_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'server_pictures_publish'


class ServerPolls(models.Model):
    code_name = models.CharField(max_length=255)
    room_id = models.IntegerField()
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    greetings_text = models.CharField(max_length=255)
    limit = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'server_polls'


class ServerPollsQuestions(models.Model):
    poll_id = models.IntegerField()
    parent_id = models.IntegerField()
    order_num = models.IntegerField()
    question = models.TextField()
    type = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'server_polls_questions'


class ServerPollsQuestionsAnswers(models.Model):
    question_id = models.IntegerField()
    value = models.TextField()
    is_correct = models.IntegerField()
    target_subquestion = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'server_polls_questions_answers'


class ServerPollsUsers(models.Model):
    poll_id = models.IntegerField()
    timestamp = models.CharField(max_length=255)
    user_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'server_polls_users'


class ServerPollsUsersAnswers(models.Model):
    main_id = models.IntegerField()
    question_id = models.IntegerField()
    answer_data = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'server_polls_users_answers'


class ServerRewardLogs(models.Model):
    user_id = models.IntegerField()
    reward_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'server_reward_logs'


class ServerRewards(models.Model):
    reward_start = models.IntegerField()
    reward_end = models.IntegerField()
    reward_type = models.CharField(max_length=8)
    reward_data = models.CharField(max_length=255)
    message = models.CharField(max_length=255)
    enabled = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'server_rewards'


class ServerSettings(models.Model):
    variable = models.CharField(primary_key=True, max_length=255)
    value = models.TextField()
    description = models.TextField()

    class Meta:
        managed = False
        db_table = 'server_settings'


class ServerStatus(models.Model):
    users_online = models.IntegerField(unique=True)
    loaded_rooms = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'server_status'


class Settings(models.Model):
    uotw = models.CharField(max_length=255, blank=True, null=True)
    notice = models.CharField(max_length=255, blank=True, null=True)
    maintenance = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'settings'


class SleeveSettings(models.Model):
    www = models.CharField(max_length=50, blank=True, null=True)
    sitename = models.CharField(max_length=50, blank=True, null=True)
    shortname = models.CharField(max_length=30, blank=True, null=True)
    slogan = models.CharField(max_length=50, blank=True, null=True)
    rpmode = models.CharField(max_length=1, blank=True, null=True)
    c_images = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sleeve_settings'


class Staffapps(models.Model):
    appid = models.AutoField(db_column='AppID', primary_key=True)  # Field name made lowercase.
    realname = models.CharField(db_column='RealName', max_length=75)  # Field name made lowercase.
    username = models.CharField(db_column='UserName', max_length=75, blank=True, null=True)  # Field name made lowercase.
    age = models.IntegerField(db_column='Age', blank=True, null=True)  # Field name made lowercase.
    timezone = models.CharField(db_column='Timezone', max_length=10, blank=True, null=True)  # Field name made lowercase.
    experience = models.TextField(db_column='Experience', blank=True, null=True)  # Field name made lowercase.
    why = models.TextField(db_column='Why', blank=True, null=True)  # Field name made lowercase.
    what = models.TextField(db_column='What', blank=True, null=True)  # Field name made lowercase.
    timestamp = models.IntegerField(db_column='TimeStamp', blank=True, null=True)  # Field name made lowercase.
    ip = models.CharField(db_column='IP', max_length=15, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'staffapps'


class Stafflogs(models.Model):
    action = models.CharField(max_length=12)
    message = models.TextField(blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    userid = models.IntegerField()
    targetid = models.IntegerField(blank=True, null=True)
    timestamp = models.CharField(max_length=50, blank=True, null=True)
    details = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'stafflogs'


class Subscriptions(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    badge_code = models.CharField(max_length=10)
    credits = models.IntegerField()
    duckets = models.IntegerField()
    respects = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'subscriptions'


class Talents(models.Model):
    type = models.CharField(max_length=11)
    level = models.IntegerField(blank=True, null=True)
    data_actions = models.TextField()
    data_gifts = models.TextField()

    class Meta:
        managed = False
        db_table = 'talents'


class TalentsSubLevels(models.Model):
    talent_level = models.IntegerField()
    sub_level = models.IntegerField()
    badge_code = models.CharField(max_length=45)
    required_progress = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'talents_sub_levels'


class Track(models.Model):
    id = models.AutoField(unique=True)
    ref = models.CharField(max_length=250)
    agent = models.CharField(max_length=250, blank=True, null=True)
    ip = models.CharField(max_length=20)
    tracking_page_code = models.CharField(max_length=100, blank=True, null=True)
    tracking_page_name = models.CharField(max_length=100, blank=True, null=True)
    dt = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'track'


class UserAchievements(models.Model):
    userid = models.PositiveIntegerField(primary_key=True)
    group = models.CharField(max_length=255)
    level = models.IntegerField()
    progress = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'user_achievements'
        unique_together = (('userid', 'group'),)


class UserAuthTicket(models.Model):
    user_id = models.IntegerField(primary_key=True)
    auth_ticket = models.CharField(max_length=60)

    class Meta:
        managed = False
        db_table = 'user_auth_ticket'


class UserBadges(models.Model):
    user_id = models.PositiveIntegerField()
    badge_id = models.CharField(max_length=100)
    badge_slot = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'user_badges'


class UserClothing(models.Model):
    user_id = models.IntegerField()
    part_id = models.CharField(max_length=25)
    part = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'user_clothing'


class UserEffects(models.Model):
    user_id = models.PositiveIntegerField(blank=True, null=True)
    effect_id = models.IntegerField(blank=True, null=True)
    total_duration = models.IntegerField(blank=True, null=True)
    is_activated = models.CharField(max_length=1, blank=True, null=True)
    activated_stamp = models.FloatField(blank=True, null=True)
    quantity = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_effects'


class UserFastfood(models.Model):
    user_id = models.IntegerField(primary_key=True)
    auth_ticket = models.CharField(max_length=95)
    powerup_sheilds = models.IntegerField()
    powerup_rockets = models.IntegerField()
    powerup_parachutes = models.IntegerField()
    games_played = models.IntegerField()
    games_won = models.IntegerField()
    games_lost = models.IntegerField()
    weekly_score = models.IntegerField()
    previous_score = models.IntegerField()
    total_score = models.IntegerField()
    last_login = models.FloatField()

    class Meta:
        managed = False
        db_table = 'user_fastfood'


class UserFavorites(models.Model):
    user_id = models.PositiveIntegerField()
    room_id = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'user_favorites'


class UserHomes(models.Model):
    username = models.CharField(primary_key=True, max_length=255)
    content = models.TextField()

    class Meta:
        managed = False
        db_table = 'user_homes'


class UserIgnores(models.Model):
    user_id = models.PositiveIntegerField()
    ignore_id = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'user_ignores'


class UserInfo(models.Model):
    user_id = models.IntegerField(primary_key=True)
    bans = models.IntegerField()
    cautions = models.IntegerField()
    reg_timestamp = models.FloatField()
    login_timestamp = models.FloatField()
    cfhs = models.IntegerField()
    cfhs_abusive = models.IntegerField()
    trading_locked = models.FloatField()
    trading_locks_count = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'user_info'


class UserLottery(models.Model):
    user_id = models.IntegerField()
    firstrare = models.TextField(db_column='FirstRare')  # Field name made lowercase.
    secondrare = models.TextField(db_column='SecondRare')  # Field name made lowercase.
    thirdrare = models.TextField(db_column='ThirdRare')  # Field name made lowercase.
    fourthrare = models.TextField(db_column='FourthRare')  # Field name made lowercase.
    rolled = models.DateTimeField(db_column='Rolled')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'user_lottery'


class UserMail(models.Model):
    sender_id = models.TextField()
    reciever_id = models.TextField()
    subject = models.TextField()
    content = models.TextField()
    trash = models.IntegerField()
    opened = models.IntegerField()
    mailed_on = models.TextField()
    reported = models.IntegerField()
    checked = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'user_mail'


class UserOnline(models.Model):
    userid = models.PositiveIntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'user_online'


class UserPresents(models.Model):
    item_id = models.PositiveIntegerField()
    base_id = models.PositiveIntegerField()
    extra_data = models.TextField()

    class Meta:
        managed = False
        db_table = 'user_presents'


class UserQuests(models.Model):
    user_id = models.PositiveIntegerField(primary_key=True)
    quest_id = models.PositiveIntegerField()
    progress = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_quests'
        unique_together = (('user_id', 'quest_id'),)


class UserRankings(models.Model):
    userid = models.IntegerField()
    type = models.CharField(max_length=1000)
    information = models.CharField(max_length=1000)
    achievement_id = models.IntegerField()
    roomid = models.IntegerField()
    score = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'user_rankings'


class UserRelationships(models.Model):
    user_id = models.IntegerField()
    target = models.IntegerField()
    type = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'user_relationships'


class UserRoomvisits(models.Model):
    user_id = models.PositiveIntegerField()
    room_id = models.PositiveIntegerField()
    entry_timestamp = models.FloatField()
    exit_timestamp = models.FloatField()
    hour = models.IntegerField()
    minute = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'user_roomvisits'


class UserSavedSearches(models.Model):
    user_id = models.IntegerField()
    filter = models.CharField(max_length=65)
    search_code = models.CharField(max_length=65)

    class Meta:
        managed = False
        db_table = 'user_saved_searches'


class UserStats(models.Model):
    id = models.IntegerField(primary_key=True)
    roomvisits = models.IntegerField(db_column='RoomVisits')  # Field name made lowercase.
    onlinetime = models.IntegerField(db_column='OnlineTime')  # Field name made lowercase.
    respect = models.IntegerField(db_column='Respect')  # Field name made lowercase.
    respectgiven = models.IntegerField(db_column='RespectGiven')  # Field name made lowercase.
    giftsgiven = models.IntegerField(db_column='GiftsGiven')  # Field name made lowercase.
    giftsreceived = models.IntegerField(db_column='GiftsReceived')  # Field name made lowercase.
    dailyrespectpoints = models.IntegerField(db_column='DailyRespectPoints')  # Field name made lowercase.
    dailypetrespectpoints = models.IntegerField(db_column='DailyPetRespectPoints')  # Field name made lowercase.
    achievementscore = models.IntegerField(db_column='AchievementScore')  # Field name made lowercase.
    quest_id = models.PositiveIntegerField()
    quest_progress = models.IntegerField()
    lev_builder = models.IntegerField()
    lev_social = models.IntegerField()
    lev_identity = models.IntegerField()
    lev_explore = models.IntegerField()
    groupid = models.IntegerField()
    tickets_answered = models.IntegerField()
    respectstimestamp = models.CharField(db_column='respectsTimestamp', max_length=6, blank=True, null=True)  # Field name made lowercase.
    forum_posts = models.IntegerField()
    userid = models.IntegerField()
    punches_thrown = models.IntegerField(blank=True, null=True)
    arrests = models.IntegerField(blank=True, null=True)
    lotterys_won = models.IntegerField()
    lottery_prize = models.IntegerField()
    rolled = models.DateTimeField(db_column='Rolled')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'user_stats'


class UserSubscriptions(models.Model):
    user_id = models.PositiveIntegerField(primary_key=True)
    subscription_id = models.CharField(max_length=20)
    timestamp_activated = models.IntegerField()
    timestamp_expire = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'user_subscriptions'


class UserTags(models.Model):
    user_id = models.PositiveIntegerField()
    tag = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'user_tags'


class UserTickets(models.Model):
    userid = models.PositiveIntegerField(unique=True)
    sessionticket = models.CharField(primary_key=True, max_length=100)
    ipaddress = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'user_tickets'
        unique_together = (('sessionticket', 'ipaddress'),)


class UserVouchers(models.Model):
    user_id = models.IntegerField()
    voucher = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'user_vouchers'
        unique_together = (('user_id', 'voucher'),)


class UserWardrobe(models.Model):
    user_id = models.PositiveIntegerField()
    slot_id = models.PositiveIntegerField()
    look = models.CharField(max_length=120)
    gender = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'user_wardrobe'


class Users(models.Model):
    username = models.CharField(unique=True, max_length=125)
    password = models.CharField(max_length=255, blank=True, null=True)
    mail = models.CharField(max_length=255, blank=True, null=True)
    auth_ticket = models.CharField(max_length=60)
    rank = models.PositiveIntegerField(blank=True, null=True)
    rank_vip = models.IntegerField(blank=True, null=True)
    credits = models.IntegerField(blank=True, null=True)
    vip_points = models.IntegerField(blank=True, null=True)
    activity_points = models.IntegerField(blank=True, null=True)
    look = models.CharField(max_length=255, blank=True, null=True)
    gender = models.CharField(max_length=1, blank=True, null=True)
    motto = models.CharField(max_length=50, blank=True, null=True)
    account_created = models.CharField(max_length=12, blank=True, null=True)
    last_online = models.IntegerField(blank=True, null=True)
    online = models.CharField(max_length=1, blank=True, null=True)
    ip_last = models.CharField(max_length=45, blank=True, null=True)
    ip_reg = models.CharField(max_length=45, blank=True, null=True)
    home_room = models.IntegerField(blank=True, null=True)
    is_muted = models.CharField(max_length=1, blank=True, null=True)
    block_newfriends = models.CharField(max_length=1, blank=True, null=True)
    hide_online = models.CharField(max_length=1, blank=True, null=True)
    hide_inroom = models.CharField(max_length=1, blank=True, null=True)
    vip = models.CharField(max_length=1, blank=True, null=True)
    volume = models.CharField(max_length=15, blank=True, null=True)
    last_change = models.IntegerField(blank=True, null=True)
    machine_id = models.CharField(max_length=125, blank=True, null=True)
    focus_preference = models.CharField(max_length=1, blank=True, null=True)
    chat_preference = models.CharField(max_length=1, blank=True, null=True)
    pets_muted = models.CharField(max_length=1, blank=True, null=True)
    bots_muted = models.CharField(max_length=1, blank=True, null=True)
    advertising_report_blocked = models.CharField(max_length=1, blank=True, null=True)
    gotw_points = models.IntegerField(blank=True, null=True)
    ignore_invites = models.CharField(max_length=1, blank=True, null=True)
    time_muted = models.FloatField(blank=True, null=True)
    allow_gifts = models.CharField(max_length=1, blank=True, null=True)
    trading_locked = models.FloatField(blank=True, null=True)
    friend_bar_state = models.CharField(max_length=1)
    disable_forced_effects = models.CharField(max_length=1)
    allow_mimic = models.CharField(max_length=1)
    working = models.CharField(max_length=50)
    secretcode = models.CharField(max_length=50)
    mymusik = models.CharField(max_length=50)
    real_name = models.CharField(max_length=100)
    visibility = models.CharField(max_length=50)
    active_players = models.CharField(max_length=999, blank=True, null=True)
    seckey = models.CharField(max_length=999)
    facebook_id = models.CharField(max_length=50)
    facebook = models.CharField(max_length=200)
    staff_twitter = models.CharField(max_length=50, blank=True, null=True)
    staff_facebook = models.CharField(max_length=50, blank=True, null=True)
    staff_pin = models.CharField(max_length=50, blank=True, null=True)
    forgot_ticket = models.CharField(max_length=50, blank=True, null=True)
    pin = models.CharField(max_length=50, blank=True, null=True)
    facebook_change = models.CharField(max_length=50, blank=True, null=True)
    staff_background_url = models.TextField(blank=True, null=True)
    staff_ocult = models.CharField(max_length=50, blank=True, null=True)
    role = models.CharField(max_length=50, blank=True, null=True)
    country_cf = models.CharField(max_length=50, blank=True, null=True)
    last_used = models.CharField(max_length=50, blank=True, null=True)
    refer_count = models.CharField(max_length=50, blank=True, null=True)
    staff_profileimage_url = models.CharField(max_length=150, blank=True, null=True)
    cblueits = models.CharField(max_length=50)
    getmoney_date = models.CharField(max_length=20)
    lotterys_won = models.IntegerField()
    lottery_prize = models.IntegerField()
    rolled = models.DateTimeField(db_column='Rolled')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'users'
        unique_together = (('id', 'auth_ticket'),)


class UsersReferidos(models.Model):
    usuario = models.CharField(max_length=400)
    ip_referida = models.CharField(max_length=50)
    fecha = models.TextField()

    class Meta:
        managed = False
        db_table = 'users_referidos'


class Values(models.Model):
    name = models.CharField(max_length=100)
    img = models.CharField(max_length=100)
    price = models.IntegerField()
    timestamp = models.IntegerField()
    who = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'values'


class Vault(models.Model):
    code = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'vault'


class VaultEntries(models.Model):
    username = models.CharField(max_length=211)
    code = models.CharField(max_length=211)

    class Meta:
        managed = False
        db_table = 'vault_entries'


class VaultPrizes(models.Model):
    name = models.CharField(max_length=211)
    amount = models.CharField(max_length=10)
    imagename = models.CharField(max_length=211)
    type = models.CharField(max_length=5)
    extradata = models.CharField(max_length=211)
    base_item = models.CharField(max_length=211)

    class Meta:
        managed = False
        db_table = 'vault_prizes'


class VaultWinners(models.Model):
    username = models.CharField(max_length=211)
    code = models.CharField(max_length=211)
    claimed = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'vault_winners'


class WiredItems(models.Model):
    id = models.IntegerField(primary_key=True)
    items = models.CharField(max_length=5000)
    delay = models.IntegerField()
    string = models.CharField(max_length=5000)
    bool = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'wired_items'


class Wordfilter(models.Model):
    word = models.CharField(primary_key=True, max_length=100)
    replacement = models.CharField(max_length=255)
    strict = models.CharField(max_length=1)
    addedby = models.CharField(max_length=100)
    bannable = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'wordfilter'
