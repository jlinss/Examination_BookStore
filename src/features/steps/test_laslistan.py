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

@then("ska katalogsidan visas")
def verify_katalog(page):
    page.get_by_text("Katalog", exact=True).first.wait_for()
    assert page.locator("body").inner_text().strip() != ""


# -------------------------
# MINA BÖCKER (FAVORITER)
# -------------------------

@then("ska sidan Mina böcker visas")
def verify_mina_bocker(page):
    page.get_by_text("Mina böcker", exact=True).first.wait_for()
    assert page.locator("body").inner_text().strip() != ""


@when("användaren öppnar Mina böcker")
def open_mina_bocker(page):
    page.get_by_text("Mina böcker", exact=True).first.click()


@then("ska favoritboken visas")
def verify_favorite_book(page):
    page.get_by_text("Dina favoriter:", exact=True).wait_for()


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
    print("Inputs:", page.locator("input").count())
    print("Valores:", page.locator("input").evaluate_all(
        "(elements) => elements.map(e => e.value)"
    ))

    page.get_by_role("button", name="Lägg till ny bok").click()

    page.wait_for_timeout(1000)

    print("URL:", page.url)
    print("Conteúdo:", page.locator("body").inner_text())
    print("Inputs:", page.locator("input").count())
    print("Valores:", page.locator("input").evaluate_all(
        "(elements) => elements.map(e => e.value)"
    ))

@then(parsers.parse('ska boken "{title}" visas på sidan'))
def verify_book_added(page, title):
    page.get_by_text("Katalog", exact=True).first.click()

    # Kontrollera att bokens titel visas i katalogen
    page.get_by_text(title, exact=False).wait_for(timeout=5000)
