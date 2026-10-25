from pytest_bdd import scenarios, given, when, then, parsers

scenarios("../katalog.feature")
scenarios("../lagg_till_bok.feature")
scenarios("../mina_bocker.feature")


# -------------------------
# Alla tester ska använda detta
# -------------------------

@given("att användaren öppnar Läslistan")
def open_laslistan(page):
    page.goto(
        "https://tap-vt26-testautomatisering.github.io/exam/",
        wait_until="domcontentloaded"
    )


@when(parsers.parse('användaren klickar på "{link_text}"'))
def click_navigation_link(page, link_text):
    page.get_by_text(link_text, exact=True).first.click()


# -------------------------
# KATALOG
# -------------------------

@when("katalogsidan har laddats")
def catalog_page_loaded(page):
    page.get_by_text(
        "Sidan för dig som gillar att läsa. Välj dina favoriter."
    ).wait_for()


@then("ska katalogsidan visas")
def verify_katalog(page):
    page.get_by_text(
        "Sidan för dig som gillar att läsa. Välj dina favoriter."
    ).wait_for()


# -------------------------
# MINA BÖCKER (FAVORITER)
# -------------------------

@then("ska sidan Mina böcker visas")
def verify_mina_bocker(page):
    page.get_by_text("Mina böcker", exact=True).first.wait_for()


@when("användaren öppnar Mina böcker")
def open_mina_bocker(page):
    page.get_by_text("Mina böcker", exact=True).first.click()


@then("ska båda favoritböckerna visas")
def verify_both_favorite_books(page):
    page.get_by_text(
        "Ormar på ett plan: En Python-berättelse",
        exact=False
    ).wait_for()

    page.get_by_text(
        "The Pragmatic Procrastinator",
        exact=False
    ).wait_for()


@then("ska den borttagna boken inte visas")
def verify_removed_book_not_visible(page):
    removed_book = page.get_by_text(
        "The Pragmatic Procrastinator",
        exact=False
    )
    assert removed_book.count() == 0


@then("ska den andra favoritboken fortfarande visas")
def verify_other_favorite_book_visible(page):
    page.get_by_text(
        "Ormar på ett plan: En Python-berättelse",
        exact=False
    ).wait_for()


@when("användaren markerar två böcker som favoriter")
def mark_two_books_as_favorites(page):
    page.get_by_test_id(
        "star-Ormar på ett plan: En Python-berättelse"
    ).click()

    page.get_by_test_id(
        "star-The Pragmatic Procrastinator"
    ).click()


@when("användaren tar bort en av favoritböckerna")
def remove_one_favorite_book(page):
    page.get_by_test_id(
        "star-The Pragmatic Procrastinator"
    ).click()


# -------------------------
# STATISTIK
# -------------------------

@then("ska statistiksidan visas")
def verify_statistik(page):
    page.get_by_text("Statistik", exact=True).first.wait_for()
    assert page.locator("body").inner_text().strip() != ""


# -------------------------
# LÄGG TILL BOK
# -------------------------


@when("användaren öppnar formuläret för att lägga till en bok")
def open_add_book_form(page):
    page.get_by_text("Lägg till bok", exact=True).first.click()


@then("ska formuläret för att lägga till en bok visas")
def verify_add_book_form(page):
    inputs = page.locator("input")
    assert inputs.count() >= 2, (
        "Formuläret innehåller inte minst två input-fält."
    )


@then("ska knappen för att lägga till boken vara inaktiverad")
def verify_add_book_button_disabled(page):
    button = page.get_by_role(
        "button",
        name="Lägg till ny bok"
    )


@when(
    parsers.parse(
        'användaren fyller i titeln "{title}" och författaren "{author}"'
    )
)
def fill_book_form(page, title, author):
    page.get_by_label("Titel").fill(title)
    page.get_by_label("Författare").fill(author)


@when("användaren klickar på knappen för att lägga till boken")
def click_add_book_button(page):
    page.get_by_role(
        "button",
        name="Lägg till ny bok"
    ).click()


@then(parsers.parse('ska boken "{title}" visas på sidan'))
def verify_book_added(page, title):
    page.get_by_text("Katalog", exact=True).first.click()
    page.get_by_text(title, exact=False).wait_for(timeout=5000)
