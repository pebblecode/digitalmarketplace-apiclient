from dmapiclient import api_stubs


def test_framework():
    assert api_stubs.framework() == {
        "frameworks": {
            "clarificationQuestionsOpen": True,
            "lots": [],
            "name": "G-Cloud 7",
            "slug": "g-cloud-7",
            "status": "open",
        }
    }


def test_framework_name_changes_with_slug():
    assert api_stubs.framework(slug='digital-outcomes-and-specialists')["frameworks"]["name"] == \
        "Digital Outcomes and Specialists"
    assert api_stubs.framework(slug="my-framework")["frameworks"]["name"] == "My Framework"


def test_lot_name_default_is_made_from_slug():
    assert api_stubs.lot(slug="my-lot")["name"] == "My Lot"


def test_lot():
    assert api_stubs.lot(slug="foo") == {
        "id": 1,
        "slug": "foo",
        "name": "Foo",
        "allowsBrief": False,
        "oneServiceLimit": False,
    }


def test_brief():
    assert api_stubs.brief() \
        == {
        "briefs": {
            "id": 1234,
            "title": "I need a thing to do a thing",
            "frameworkSlug": "digital-outcomes-and-specialists",
            "lotSlug": "digital-specialists",
            "status": "draft",
            "users": [{"active": True,
                       "role": "buyer",
                       "emailAddress": "buyer@email.com",
                       "id": 123,
                       "name": "Buyer User"}],
            "createdAt": "2016-03-29T10:11:12.000000Z",
            "updatedAt": "2016-03-29T10:11:13.000000Z"
        }
    }

    assert api_stubs.brief(status='live', framework_slug='a-framework-slug', lot_slug='a-lot-slug', user_id=234) \
        == {
        "briefs": {
            "id": 1234,
            "title": "I need a thing to do a thing",
            "frameworkSlug": "a-framework-slug",
            "lotSlug": "a-lot-slug",
            "status": "live",
            "users": [{"active": True,
                       "role": "buyer",
                       "emailAddress": "buyer@email.com",
                       "id": 234,
                       "name": "Buyer User"}],
            "createdAt": "2016-03-29T10:11:12.000000Z",
            "updatedAt": "2016-03-29T10:11:13.000000Z",
            "publishedAt": "2016-03-29T10:11:14.000000Z"
        }
    }
