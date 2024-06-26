import builtins

import pytest

import elevator


@pytest.mark.parametrize("input_values, expected",
                         [(["2", "3", "3", "0", "1"], "8"),
                          (["5", "1", "71"], "30"),
                          (['3', '100', '0', '2', '2', '0', '0', '0', '2', '2', '0', '2', '0', '0', '1', '0', '0', '2', '0', '0', '2', '2', '0', '0', '2', '1', '1', '0', '0', '0', '1', '0', '0', '0', '0', '0', '1', '1', '2', '0', '0', '0', '1', '0', '0', '0', '0', '0', '0', '0', '1', '0', '0', '0', '1', '1', '0', '2', '0', '0', '0', '2', '0', '0', '0', '2', '0', '1', '0', '1', '0', '2', '2', '1', '2', '0', '0', '0', '0', '2', '0', '0', '0', '2', '0', '2', '0', '2', '0', '2', '0', '1', '0', '0', '2', '0', '2', '1', '2', '0', '1', '0'], "2286"),
                          (['4695', '100', '89', '21', '63', '61', '75', '28', '89', '86', '60', '39', '81', '3', '85', '60', '89', '86', '85', '51', '60', '15', '56', '24', '90', '6', '4', '53', '34', '35', '22', '88', '17', '8', '45', '6', '28', '85', '35', '60', '8', '82', '72', '29', '26', '78', '52', '98', '78', '25', '43', '81', '35', '94', '23', '3', '50', '2', '46', '51', '82', '95', '86', '47', '13', '18', '4', '77', '52', '66', '49', '13', '9', '64', '32', '70', '50', '53', '74', '0', '8', '4', '28', '41', '88', '99', '40', '64', '74', '97', '84', '60', '6', '21', '48', '7', '37', '6', '31', '0', '0', '0'], "194"),
                          (['50', '100', '52', '59', '45', '7', '6', '56', '55', '7', '60', '10', '51', '59', '97', '56', '49', '6', '43', '7', '45', '9', '54', '43', '7', '46', '9', '8', '41', '50', '41', '43', '47', '51', '7', '54', '9', '7', '1', '48', '59', '60', '2', '9', '43', '47', '58', '52', '57', '47', '54', '57', '50', '47', '3', '51', '44', '48', '3', '60', '6', '58', '58', '47', '52', '7', '3', '90', '4', '46', '53', '57', '8', '3', '59', '59', '47', '7', '1', '41', '52', '9', '55', '6', '43', '3', '42', '52', '49', '49', '3', '39', '0', '50', '48', '6', '4', '46', '50', '9', '59', '60'], "7278"),
                          (['6', '100', '60', '18', '1', '1', '50', '14', '33', '39', '10', '28', '23', '29', '24', '36', '13', '79', '80', '56', '81', '75', '64', '76', '29', '65', '84', '60', '43', '85', '80', '56', '57', '69', '10', '76', '5', '29', '84', '72', '67', '25', '56', '14', '15', '27', '10', '58', '5', '23', '48', '6', '31', '55', '32', '2', '99', '63', '28', '58', '83', '5', '30', '60', '13', '61', '8', '26', '27', '69', '28', '46', '29', '65', '96', '24', '37', '13', '80', '86', '93', '33', '88', '82', '77', '41', '84', '72', '73', '1', '86', '56', '39', '75', '64', '82', '95', '89', '90', '0', '79', '1'], "87308"),
                          (['100', '100', '99', '98', '97', '96', '95', '94', '93', '92', '91', '90', '89', '88', '87', '86', '85', '84', '83', '82', '81', '80', '79', '78', '77', '76', '75', '74', '73', '72', '71', '70', '69', '68', '67', '66', '65', '64', '63', '62', '61', '60', '59', '58', '57', '56', '55', '54', '53', '52', '51', '50', '49', '48', '47', '46', '45', '44', '43', '42', '41', '40', '39', '38', '37', '36', '35', '34', '33', '32', '31', '30', '29', '28', '27', '26', '25', '24', '23', '22', '21', '20', '19', '18', '17', '16', '15', '14', '13', '12', '11', '10', '9', '8', '7', '6', '5', '4', '3', '2', '1', '0'], "3436")])
def test_elevator(capsys, monkeypatch, input_values, expected):
    info = iter(input_values)
    monkeypatch.setattr(builtins, "input", lambda: next(info))
    elevator.time_elevator()
    answer = capsys.readouterr().out.strip()
    assert answer == expected
