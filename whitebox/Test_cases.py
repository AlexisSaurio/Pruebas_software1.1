
"""
White-box unit testing examples.
"""
import unittest
from unittest.mock import MagicMock, patch

from class_exercises import (check_number_status,validate_password,
calculate_total_discount,calculate_order_total,calculate_items_shipping_cost,
validate_login,verify_age,categorize_product,validate_email,celsius_to_fahrenheit,validate_credit_card,validate_date,
check_flight_eligibility,validate_url,calculate_quantity_discount,check_file_size,check_loan_eligibility,calculate_shipping_cost,
grade_quiz,authenticate_user,get_weather_advisory,VendingMachine,UserAuthentication,TrafficLight,DocumentEditingSystem,ElevatorSystem
,ShoppingCart,BankingSystem
)


class TestWhiteBox(unittest.TestCase):

    # EJERCICIO 1
    def test_check_number_positive(self):
        self.assertEqual(check_number_status(10), "Positive")

    def test_check_number_boundary_one(self):
        self.assertEqual(check_number_status(1), "Positive")

    def test_check_number_negative(self):
        self.assertEqual(check_number_status(-5), "Negative")

    def test_check_number_boundary_minus_one(self):
        self.assertEqual(check_number_status(-1), "Negative")

    def test_check_number_zero(self):
        self.assertEqual(check_number_status(0), "Zero")

    # EJERCICIO 2
    def test_validate_password_valid(self):
        self.assertTrue(validate_password("Valid1Pass!"))

    def test_validate_password_boundary_7_chars(self):
        self.assertFalse(validate_password("Sh0rt!x"))

    def test_validate_password_boundary_8_chars_valid(self):
        self.assertTrue(validate_password("Valid1A!"))

    def test_validate_password_missing_uppercase(self):
        self.assertFalse(validate_password("nouppercase1!"))

    def test_validate_password_missing_lowercase(self):
        self.assertFalse(validate_password("NOLOWERCASE1!"))

    def test_validate_password_missing_digit(self):
        self.assertFalse(validate_password("NoDigitHere!"))

    def test_validate_password_missing_special_char(self):
        self.assertFalse(validate_password("NoSpecialChar1"))

    def test_validate_password_special_char_at(self):
        self.assertTrue(validate_password("Valid1Pa@"))

    def test_validate_password_special_char_hash(self):
        self.assertTrue(validate_password("Valid1Pa#"))

    def test_validate_password_special_char_dollar(self):
        self.assertTrue(validate_password("Valid1Pa$"))

    def test_validate_password_special_char_percent(self):
        self.assertTrue(validate_password("Valid1Pa%"))

    def test_validate_password_special_char_ampersand(self):
        self.assertTrue(validate_password("Valid1Pa&"))

    # EJERCICIO 3
    def test_calculate_total_discount_below_100(self):
        self.assertEqual(calculate_total_discount(99), 0)

    def test_calculate_total_discount_boundary_100(self):
        self.assertEqual(calculate_total_discount(100), 10.0)

    def test_calculate_total_discount_mid_range(self):
        self.assertEqual(calculate_total_discount(200), 20.0)

    def test_calculate_total_discount_boundary_500(self):
        self.assertEqual(calculate_total_discount(500), 50.0)

    def test_calculate_total_discount_boundary_501(self):
        self.assertEqual(calculate_total_discount(501), 100.2)

    def test_calculate_total_discount_above_500(self):
        self.assertEqual(calculate_total_discount(600), 120.0)

    # EJERCICIO 4
    def test_calculate_order_total_boundary_5(self):
        items = [{"quantity": 5, "price": 100}]
        self.assertEqual(calculate_order_total(items), 500)

    def test_calculate_order_total_boundary_6(self):
        items = [{"quantity": 6, "price": 100}]
        self.assertAlmostEqual(calculate_order_total(items), 570.0, places=5)

    def test_calculate_order_total_mid_five_percent(self):
        items = [{"quantity": 8, "price": 100}]
        self.assertAlmostEqual(calculate_order_total(items), 760.0, places=5)

    def test_calculate_order_total_boundary_10(self):
        items = [{"quantity": 10, "price": 100}]
        self.assertAlmostEqual(calculate_order_total(items), 950.0, places=5)

    def test_calculate_order_total_boundary_11(self):
        items = [{"quantity": 11, "price": 100}]
        self.assertAlmostEqual(calculate_order_total(items), 990.0, places=5)

    def test_calculate_order_total_ten_percent(self):
        items = [{"quantity": 15, "price": 100}]
        self.assertAlmostEqual(calculate_order_total(items), 1350.0, places=5)

    def test_calculate_order_total_empty(self):
        self.assertEqual(calculate_order_total([]), 0)

    def test_calculate_order_total_multiple_items(self):
        items = [{"quantity": 3, "price": 50}, {"quantity": 8, "price": 50}]
        self.assertAlmostEqual(calculate_order_total(items), 530.0, places=5)

    # EJERCICIO 5
    def test_shipping_standard_boundary_5(self):
        self.assertEqual(calculate_items_shipping_cost([{"weight": 5}], "standard"), 10)

    def test_shipping_standard_boundary_above_5(self):
        self.assertEqual(calculate_items_shipping_cost([{"weight": 6}], "standard"), 15)

    def test_shipping_standard_boundary_10(self):
        self.assertEqual(calculate_items_shipping_cost([{"weight": 10}], "standard"), 15)

    def test_shipping_standard_heavy(self):
        self.assertEqual(calculate_items_shipping_cost([{"weight": 12}], "standard"), 20)

    def test_shipping_express_boundary_5(self):
        self.assertEqual(calculate_items_shipping_cost([{"weight": 5}], "express"), 20)

    def test_shipping_express_medium(self):
        self.assertEqual(calculate_items_shipping_cost([{"weight": 8}], "express"), 30)

    def test_shipping_express_boundary_10(self):
        self.assertEqual(calculate_items_shipping_cost([{"weight": 10}], "express"), 30)

    def test_shipping_express_heavy(self):
        self.assertEqual(calculate_items_shipping_cost([{"weight": 12}], "express"), 40)

    def test_shipping_multiple_items_combined_weight(self):
        self.assertEqual(calculate_items_shipping_cost([{"weight": 3}, {"weight": 4}], "standard"), 15)

    def test_shipping_invalid_method(self):
        with self.assertRaises(ValueError):
            calculate_items_shipping_cost([{"weight": 5}], "drone")

    def test_shipping_empty_string_method(self):
        with self.assertRaises(ValueError):
            calculate_items_shipping_cost([{"weight": 5}], "")

    # EJERCICIO 6
    def test_validate_login_success(self):
        self.assertEqual(validate_login("admin1", "password12"), "Login Successful")

    def test_validate_login_username_boundary_5(self):
        self.assertEqual(validate_login("user1", "password12"), "Login Successful")

    def test_validate_login_username_boundary_20(self):
        self.assertEqual(validate_login("a" * 20, "password12"), "Login Successful")

    def test_validate_login_username_too_short(self):
        self.assertEqual(validate_login("usr", "password12"), "Login Failed")

    def test_validate_login_username_too_long(self):
        self.assertEqual(validate_login("a" * 21, "password12"), "Login Failed")

    def test_validate_login_password_boundary_8(self):
        self.assertEqual(validate_login("admin1", "pass1234"), "Login Successful")

    def test_validate_login_password_boundary_15(self):
        self.assertEqual(validate_login("admin1", "a" * 15), "Login Successful")

    def test_validate_login_password_too_short(self):
        self.assertEqual(validate_login("admin1", "pass"), "Login Failed")

    def test_validate_login_password_too_long(self):
        self.assertEqual(validate_login("admin1", "a" * 16), "Login Failed")

    # EJERCICIO 7
    def test_verify_age_mid_eligible(self):
        self.assertEqual(verify_age(25), "Eligible")

    def test_verify_age_boundary_18(self):
        self.assertEqual(verify_age(18), "Eligible")

    def test_verify_age_boundary_65(self):
        self.assertEqual(verify_age(65), "Eligible")

    def test_verify_age_boundary_17(self):
        self.assertEqual(verify_age(17), "Not Eligible")

    def test_verify_age_boundary_66(self):
        self.assertEqual(verify_age(66), "Not Eligible")

    # EJERCICIO 8
    def test_categorize_product_boundary_10(self):
        self.assertEqual(categorize_product(10), "Category A")

    def test_categorize_product_boundary_50(self):
        self.assertEqual(categorize_product(50), "Category A")

    def test_categorize_product_boundary_51(self):
        self.assertEqual(categorize_product(51), "Category B")

    def test_categorize_product_boundary_100(self):
        self.assertEqual(categorize_product(100), "Category B")

    def test_categorize_product_boundary_101(self):
        self.assertEqual(categorize_product(101), "Category C")

    def test_categorize_product_boundary_200(self):
        self.assertEqual(categorize_product(200), "Category C")

    def test_categorize_product_boundary_201(self):
        self.assertEqual(categorize_product(201), "Category D")

    def test_categorize_product_below_10(self):
        self.assertEqual(categorize_product(5), "Category D")

    # EJERCICIO 9
    def test_validate_email_valid(self):
        self.assertEqual(validate_email("test@domain.com"), "Valid Email")

    def test_validate_email_boundary_5_chars(self):
        self.assertEqual(validate_email("a@b.c"), "Valid Email")

    def test_validate_email_too_short(self):
        self.assertEqual(validate_email("a@b."), "Invalid Email")

    def test_validate_email_too_long(self):
        self.assertEqual(validate_email("a" * 50 + "@b.com"), "Invalid Email")

    def test_validate_email_missing_at(self):
        self.assertEqual(validate_email("testdomain.com"), "Invalid Email")

    def test_validate_email_missing_dot(self):
        self.assertEqual(validate_email("test@domaincom"), "Invalid Email")

    def test_validate_email_empty(self):
        self.assertEqual(validate_email(""), "Invalid Email")

    # EJERCICIO 10
    def test_celsius_zero(self):
        self.assertEqual(celsius_to_fahrenheit(0), 32.0)

    def test_celsius_boundary_100(self):
        self.assertEqual(celsius_to_fahrenheit(100), 212.0)

    def test_celsius_boundary_minus_100(self):
        self.assertEqual(celsius_to_fahrenheit(-100), -148.0)

    def test_celsius_boundary_101_invalid(self):
        self.assertEqual(celsius_to_fahrenheit(101), "Invalid Temperature")

    def test_celsius_boundary_minus_101_invalid(self):
        self.assertEqual(celsius_to_fahrenheit(-101), "Invalid Temperature")

    def test_celsius_mid_positive(self):
        self.assertAlmostEqual(celsius_to_fahrenheit(37), 98.6, places=5)

    def test_celsius_minus_40(self):
        self.assertEqual(celsius_to_fahrenheit(-40), -40.0)

    # EJERCICIO 11
    def test_credit_card_boundary_13_digits(self):
        self.assertEqual(validate_credit_card("1234567890123"), "Valid Card")

    def test_credit_card_boundary_16_digits(self):
        self.assertEqual(validate_credit_card("1234567890123456"), "Valid Card")

    def test_credit_card_boundary_12_invalid(self):
        self.assertEqual(validate_credit_card("123456789012"), "Invalid Card")

    def test_credit_card_boundary_17_invalid(self):
        self.assertEqual(validate_credit_card("12345678901234567"), "Invalid Card")

    def test_credit_card_contains_letter(self):
        self.assertEqual(validate_credit_card("12345678901234a"), "Invalid Card")

    def test_credit_card_contains_space(self):
        self.assertEqual(validate_credit_card("1234 5678901234"), "Invalid Card")

    # EJERCICIO 12
    def test_validate_date_valid(self):
        self.assertEqual(validate_date(2023, 10, 15), "Valid Date")

    def test_validate_date_boundary_year_1900(self):
        self.assertEqual(validate_date(1900, 1, 1), "Valid Date")

    def test_validate_date_boundary_year_2100(self):
        self.assertEqual(validate_date(2100, 12, 31), "Valid Date")

    def test_validate_date_year_before_1900(self):
        self.assertEqual(validate_date(1899, 10, 15), "Invalid Date")

    def test_validate_date_year_after_2100(self):
        self.assertEqual(validate_date(2101, 10, 15), "Invalid Date")

    def test_validate_date_month_zero(self):
        self.assertEqual(validate_date(2023, 0, 15), "Invalid Date")

    def test_validate_date_month_13(self):
        self.assertEqual(validate_date(2023, 13, 15), "Invalid Date")

    def test_validate_date_day_zero(self):
        self.assertEqual(validate_date(2023, 10, 0), "Invalid Date")

    def test_validate_date_day_32(self):
        self.assertEqual(validate_date(2023, 10, 32), "Invalid Date")

    # EJERCICIO 13
    def test_flight_eligible_by_age(self):
        self.assertEqual(check_flight_eligibility(30, False), "Eligible to Book")

    def test_flight_eligible_boundary_18(self):
        self.assertEqual(check_flight_eligibility(18, False), "Eligible to Book")

    def test_flight_eligible_boundary_65(self):
        self.assertEqual(check_flight_eligibility(65, False), "Eligible to Book")

    def test_flight_eligible_by_frequent_flyer(self):
        self.assertEqual(check_flight_eligibility(70, True), "Eligible to Book")

    def test_flight_eligible_underage_frequent_flyer(self):
        self.assertEqual(check_flight_eligibility(10, True), "Eligible to Book")

    def test_flight_not_eligible_age_17(self):
        self.assertEqual(check_flight_eligibility(17, False), "Not Eligible to Book")

    def test_flight_not_eligible_age_66(self):
        self.assertEqual(check_flight_eligibility(66, False), "Not Eligible to Book")

    # EJERCICIO 14
    def test_validate_url_valid_http(self):
        self.assertEqual(validate_url("http://example.com"), "Valid URL")

    def test_validate_url_valid_https(self):
        self.assertEqual(validate_url("https://example.com"), "Valid URL")

    def test_validate_url_http_too_long(self):
        self.assertEqual(validate_url("http://" + "a" * 250 + ".com"), "Invalid URL")

    def test_validate_url_invalid_protocol_ftp(self):
        self.assertEqual(validate_url("ftp://example.com"), "Invalid URL")

    def test_validate_url_no_protocol(self):
        self.assertEqual(validate_url("example.com"), "Invalid URL")

    def test_validate_url_http_boundary_255(self):
        self.assertEqual(validate_url("http://" + "a" * 241 + ".com"), "Valid URL")

    # EJERCICIO 15
    def test_quantity_discount_boundary_1(self):
        self.assertEqual(calculate_quantity_discount(1), "No Discount")

    def test_quantity_discount_boundary_5(self):
        self.assertEqual(calculate_quantity_discount(5), "No Discount")

    def test_quantity_discount_boundary_6(self):
        self.assertEqual(calculate_quantity_discount(6), "5% Discount")

    def test_quantity_discount_boundary_10(self):
        self.assertEqual(calculate_quantity_discount(10), "5% Discount")

    def test_quantity_discount_boundary_11(self):
        self.assertEqual(calculate_quantity_discount(11), "10% Discount")

    def test_quantity_discount_high(self):
        self.assertEqual(calculate_quantity_discount(20), "10% Discount")

    # EJERCICIO 16
    def test_file_size_boundary_zero(self):
        self.assertEqual(check_file_size(0), "Valid File Size")

    def test_file_size_boundary_max(self):
        self.assertEqual(check_file_size(1048576), "Valid File Size")

    def test_file_size_mid_valid(self):
        self.assertEqual(check_file_size(500000), "Valid File Size")

    def test_file_size_boundary_minus_1(self):
        self.assertEqual(check_file_size(-1), "Invalid File Size")

    def test_file_size_boundary_above_max(self):
        self.assertEqual(check_file_size(1048577), "Invalid File Size")

    # EJERCICIO 17
    def test_loan_not_eligible_low_income(self):
        self.assertEqual(check_loan_eligibility(20000, 800), "Not Eligible")

    def test_loan_boundary_29999_not_eligible(self):
        self.assertEqual(check_loan_eligibility(29999, 800), "Not Eligible")

    def test_loan_boundary_30000_good_credit(self):
        self.assertEqual(check_loan_eligibility(30000, 701), "Standard Loan")

    def test_loan_secured_mid_income_low_credit(self):
        self.assertEqual(check_loan_eligibility(45000, 650), "Secured Loan")

    def test_loan_boundary_credit_700_secured(self):
        self.assertEqual(check_loan_eligibility(45000, 700), "Secured Loan")

    def test_loan_boundary_credit_701_standard(self):
        self.assertEqual(check_loan_eligibility(45000, 701), "Standard Loan")

    def test_loan_boundary_60000_good_credit(self):
        self.assertEqual(check_loan_eligibility(60000, 750), "Standard Loan")

    def test_loan_boundary_credit_751_premium(self):
        self.assertEqual(check_loan_eligibility(61000, 751), "Premium Loan")

    def test_loan_boundary_credit_750_standard_high_income(self):
        self.assertEqual(check_loan_eligibility(61000, 750), "Standard Loan")

    # EJERCICIO 18
    def test_shipping_cost_small_max_bounds(self):
        self.assertEqual(calculate_shipping_cost(1, 10, 10, 10), 5)

    def test_shipping_cost_medium_min_bounds(self):
        self.assertEqual(calculate_shipping_cost(1.1, 11, 11, 11), 10)

    def test_shipping_cost_medium_max_bounds(self):
        self.assertEqual(calculate_shipping_cost(5, 30, 30, 30), 10)

    def test_shipping_cost_large(self):
        self.assertEqual(calculate_shipping_cost(10, 40, 40, 40), 20)

    def test_shipping_cost_large_weight_only(self):
        self.assertEqual(calculate_shipping_cost(6, 20, 20, 20), 20)

    def test_shipping_cost_large_length_only(self):
        self.assertEqual(calculate_shipping_cost(3, 31, 20, 20), 20)

    def test_shipping_cost_large_width_only(self):
        self.assertEqual(calculate_shipping_cost(3, 20, 31, 20), 20)

    def test_shipping_cost_large_height_only(self):
        self.assertEqual(calculate_shipping_cost(3, 20, 20, 31), 20)

    # EJERCICIO 19
    def test_grade_quiz_boundary_pass_min(self):
        self.assertEqual(grade_quiz(7, 2), "Pass")

    def test_grade_quiz_boundary_pass_zero_incorrect(self):
        self.assertEqual(grade_quiz(7, 0), "Pass")

    def test_grade_quiz_conditional_pass(self):
        self.assertEqual(grade_quiz(5, 3), "Conditional Pass")

    def test_grade_quiz_7_correct_3_incorrect_conditional(self):
        self.assertEqual(grade_quiz(7, 3), "Conditional Pass")

    def test_grade_quiz_fail_low_correct(self):
        self.assertEqual(grade_quiz(4, 4), "Fail")

    def test_grade_quiz_fail_too_many_incorrect(self):
        self.assertEqual(grade_quiz(6, 4), "Fail")

    def test_grade_quiz_fail_zero_correct(self):
        self.assertEqual(grade_quiz(0, 10), "Fail")

    # EJERCICIO 20
    def test_authenticate_admin(self):
        self.assertEqual(authenticate_user("admin", "admin123"), "Admin")

    def test_authenticate_standard_user(self):
        self.assertEqual(authenticate_user("user1", "password123"), "User")

    def test_authenticate_boundary_password_8(self):
        self.assertEqual(authenticate_user("user12", "pass1234"), "User")

    def test_authenticate_admin_wrong_password_long_enough(self):
        self.assertEqual(authenticate_user("admin", "wrongpass"), "User")

    def test_authenticate_invalid_short_username(self):
        self.assertEqual(authenticate_user("usr", "pass"), "Invalid")

    def test_authenticate_invalid_short_password(self):
        self.assertEqual(authenticate_user("user12", "pass"), "Invalid")

    def test_authenticate_admin_wrong_password_too_short(self):
        self.assertEqual(authenticate_user("admin", "wrong"), "Invalid")

    # EJERCICIO 21
    def test_weather_high_temp_high_humidity(self):
        self.assertEqual(get_weather_advisory(35, 80), "High Temperature and Humidity. Stay Hydrated.")

    def test_weather_boundary_temp_31_humidity_71(self):
        self.assertEqual(get_weather_advisory(31, 71), "High Temperature and Humidity. Stay Hydrated.")

    def test_weather_high_temp_humidity_equal_70(self):
        self.assertEqual(get_weather_advisory(35, 70), "No Specific Advisory")

    def test_weather_temp_equal_30_high_humidity(self):
        self.assertEqual(get_weather_advisory(30, 80), "No Specific Advisory")

    def test_weather_low_temperature(self):
        self.assertEqual(get_weather_advisory(-5, 50), "Low Temperature. Bundle Up!")

    def test_weather_boundary_minus_1(self):
        self.assertEqual(get_weather_advisory(-1, 50), "Low Temperature. Bundle Up!")

    def test_weather_boundary_zero_no_advisory(self):
        self.assertEqual(get_weather_advisory(0, 50), "No Specific Advisory")

    def test_weather_no_advisory(self):
        self.assertEqual(get_weather_advisory(20, 50), "No Specific Advisory")

    def test_weather_low_temp_high_humidity_low_wins(self):
        self.assertEqual(get_weather_advisory(-10, 90), "Low Temperature. Bundle Up!")


# EJERCICIO 22 
class TestWhiteBoxVendingMachine(unittest.TestCase):
    """Pruebas de caja blanca asegurando cobertura de ramas para VendingMachine."""

    def setUp(self):
        self.machine = VendingMachine()

    def test_branch_insert_coin_success(self):
        """Evalúa la rama if self.state == 'Ready'."""
        result = self.machine.insert_coin()
        self.assertEqual(result, "Coin Inserted. Select your drink.")
        self.assertEqual(self.machine.state, "Dispensing")

    def test_branch_insert_coin_fail(self):
        """Evalúa el retorno por defecto cuando state no es 'Ready'."""
        self.machine.state = "Dispensing" # Forzamos el estado
        result = self.machine.insert_coin()
        self.assertEqual(result, "Invalid operation in current state.")

    def test_branch_select_drink_success(self):
        """Evalúa la rama if self.state == 'Dispensing'."""
        self.machine.state = "Dispensing"
        result = self.machine.select_drink()
        self.assertEqual(result, "Drink Dispensed. Thank you!")
        self.assertEqual(self.machine.state, "Ready")

    def test_branch_select_drink_fail(self):
        """Evalúa el retorno por defecto cuando state no es 'Dispensing'."""
        # El estado inicial ya es "Ready"
        result = self.machine.select_drink()
        self.assertEqual(result, "Invalid operation in current state.")


# EJERCICIO 23 
class TestWhiteBoxTrafficLight(unittest.TestCase):
    """Pruebas de caja blanca asegurando cobertura de todos los if/elif para TrafficLight."""

    def setUp(self):
        self.light = TrafficLight()

    def test_branch_red_to_green(self):
        """Evalúa la rama if self.state == 'Red'."""
        self.light.state = "Red"
        self.light.change_state()
        self.assertEqual(self.light.get_current_state(), "Green")

    def test_branch_green_to_yellow(self):
        """Evalúa la rama elif self.state == 'Green'."""
        self.light.state = "Green"
        self.light.change_state()
        self.assertEqual(self.light.get_current_state(), "Yellow")

    def test_branch_yellow_to_red(self):
        """Evalúa la rama elif self.state == 'Yellow'."""
        self.light.state = "Yellow"
        self.light.change_state()
        self.assertEqual(self.light.get_current_state(), "Red")


# EJERCICIO 24 
class TestWhiteBoxUserAuthentication(unittest.TestCase):
    """Pruebas de caja blanca para estados de Login y Logout."""

    def setUp(self):
        self.auth = UserAuthentication()

    def test_branch_login_when_logged_out(self):
        """Evalúa la entrada al if de login (camino exitoso)."""
        result = self.auth.login()
        self.assertEqual(result, "Login successful")
        self.assertEqual(self.auth.state, "Logged In")

    def test_branch_login_when_logged_in(self):
        """Evalúa el rechazo del login (salto del if)."""
        self.auth.state = "Logged In"
        result = self.auth.login()
        self.assertEqual(result, "Invalid operation in current state")

    def test_branch_logout_when_logged_in(self):
        """Evalúa la entrada al if de logout (camino exitoso)."""
        self.auth.state = "Logged In"
        result = self.auth.logout()
        self.assertEqual(result, "Logout successful")
        self.assertEqual(self.auth.state, "Logged Out")

    def test_branch_logout_when_logged_out(self):
        """Evalúa el rechazo del logout (salto del if)."""
        result = self.auth.logout()
        self.assertEqual(result, "Invalid operation in current state")


# EJERCICIO 25 
class TestWhiteBoxDocumentEditingSystem(unittest.TestCase):
    """Pruebas de caja blanca evaluando transiciones de DocumentEditingSystem."""

    def setUp(self):
        self.doc_system = DocumentEditingSystem()

    def test_branch_save_document_success(self):
        """Evalúa guardar documento desde estado Editing."""
        result = self.doc_system.save_document()
        self.assertEqual(result, "Document saved successfully")
        self.assertEqual(self.doc_system.state, "Saved")

    def test_branch_save_document_fail(self):
        """Evalúa intentar guardar cuando ya está Saved."""
        self.doc_system.state = "Saved"
        result = self.doc_system.save_document()
        self.assertEqual(result, "Invalid operation in current state")

    def test_branch_edit_document_success(self):
        """Evalúa editar documento desde estado Saved."""
        self.doc_system.state = "Saved"
        result = self.doc_system.edit_document()
        self.assertEqual(result, "Editing resumed")
        self.assertEqual(self.doc_system.state, "Editing")

    def test_branch_edit_document_fail(self):
        """Evalúa intentar editar cuando ya está en Editing."""
        result = self.doc_system.edit_document()
        self.assertEqual(result, "Invalid operation in current state")


# EJERCICIO 26 
class TestWhiteBoxElevatorSystem(unittest.TestCase):
    """Pruebas de caja blanca para los condicionales del Elevador."""

    def setUp(self):
        self.elevator = ElevatorSystem()

    def test_branch_move_up_from_idle(self):
        """Evalúa el if al mover hacia arriba correctamente."""
        result = self.elevator.move_up()
        self.assertEqual(result, "Elevator moving up")
        self.assertEqual(self.elevator.state, "Moving Up")

    def test_branch_move_up_when_moving(self):
        """Evalúa el salto del if en move_up."""
        self.elevator.state = "Moving Down"
        result = self.elevator.move_up()
        self.assertEqual(result, "Invalid operation in current state")

    def test_branch_move_down_from_idle(self):
        """Evalúa el if al mover hacia abajo correctamente."""
        result = self.elevator.move_down()
        self.assertEqual(result, "Elevator moving down")
        self.assertEqual(self.elevator.state, "Moving Down")

    def test_branch_move_down_when_moving(self):
        """Evalúa el salto del if en move_down."""
        self.elevator.state = "Moving Up"
        result = self.elevator.move_down()
        self.assertEqual(result, "Invalid operation in current state")

    def test_branch_stop_from_moving_up(self):
        """Evalúa primera condición del array en stop() ['Moving Up']."""
        self.elevator.state = "Moving Up"
        result = self.elevator.stop()
        self.assertEqual(result, "Elevator stopped")

    def test_branch_stop_from_moving_down(self):
        """Evalúa segunda condición del array en stop() ['Moving Down']."""
        self.elevator.state = "Moving Down"
        result = self.elevator.stop()
        self.assertEqual(result, "Elevator stopped")

    def test_branch_stop_when_idle(self):
        """Evalúa falla al detener cuando ya está Idle."""
        result = self.elevator.stop()
        self.assertEqual(result, "Invalid operation in current state")



class TestBankingSystem(unittest.TestCase):
    def setUp(self):
        self.system = BankingSystem()
        self.username = "user123"
        self.password = "pass123"

    def test_authenticate_success(self):
        result = self.system.authenticate(self.username, self.password)
        self.assertTrue(result)
        self.assertIn(self.username, self.system.logged_in_users)

    def test_transfer_money_unauthenticated(self):
        result = self.system.transfer_money("user123", "user456", 100, "regular")
        self.assertFalse(result)

    @patch('__main__.BankAccount') 
    def test_transfer_money_insufficient_funds(self, mock_bank_class):
        self.system.logged_in_users.add(self.username)
        
        mock_instance = mock_bank_class.return_value
        mock_instance.balance = 10 
        
        result = self.system.transfer_money(self.username, "receiver", 100, "regular")
        
        self.assertFalse(result)
        mock_bank_class.assert_called_with(self.username, 1000)

    @patch('__main__.BankAccount')
    def test_transfer_money_express_success(self, mock_bank_class):
        self.system.logged_in_users.add(self.username)
        
        mock_instance = mock_bank_class.return_value
        mock_instance.balance = 5000
        
        result = self.system.transfer_money(self.username, "receiver", 100, "express")
        
        self.assertTrue(result)



class TestShoppingCart(unittest.TestCase):
    def setUp(self):
        self.cart = ShoppingCart()
        self.mock_p1 = MagicMock()
        self.mock_p1.name = "Laptop"
        self.mock_p1.price = 1000

        self.mock_p2 = MagicMock()
        self.mock_p2.name = "Mouse"
        self.mock_p2.price = 50

    def test_add_product_new_and_existing(self):
        self.cart.add_product(self.mock_p1, 1)
        self.assertEqual(len(self.cart.items), 1)
        
        self.cart.add_product(self.mock_p1, 2) 
        self.assertEqual(self.cart.items[0]["quantity"], 3)

    def test_remove_product_partial(self):
        self.cart.add_product(self.mock_p2, 5)
        self.cart.remove_product(self.mock_p2, 2)
        
        self.assertEqual(self.cart.items[0]["quantity"], 3)

    def test_remove_product_complete(self):
        self.cart.add_product(self.mock_p2, 1)
        self.cart.remove_product(self.mock_p2, 1)
        
        self.assertEqual(len(self.cart.items), 0)

    def test_checkout_calculation(self):
        self.cart.add_product(self.mock_p1, 1) 
        self.cart.add_product(self.mock_p2, 2) 
        
        
        with patch('builtins.print') as mock_print:
            self.cart.checkout()
            mock_print.assert_any_call("Total: $1100")

    
if __name__ == '__main__':
    unittest.main()