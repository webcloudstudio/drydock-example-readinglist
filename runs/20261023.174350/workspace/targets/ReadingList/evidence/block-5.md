# Evidence: Block 5 · Feature (block-5)

- block type: block
- date: 2026-10-23
- resulting state: closed/verified
- story points (combined assembled cost): 4260
- execution id: 20261023.180537.658Z-88e2571d

## Stories built
- Provide bin/test.sh and prove the complete suite passes end to end. (test-runner) [story]

## Stacked context
- stack: python_compact.md (SP 921)
- compass: COMPASS.md (SP 895)
- implements: FEATURE-TestRunner.md (SP 1546)
- context: ARCHITECTURE_compact.md (SP 424)
- context: DATABASE_compact.md (SP 317)

## Build directory changes
- bin/test.sh
- tests/test_test_runner.py

## Pre-build acceptance observation
- RED: test-runner-posix-syntax (FEATURE-TestRunner.md)
  intent: bin/test.sh exists and parses as POSIX sh without errors.
  return code: 1
  stderr:
    --- drydock: values at failure ---
      script = PosixPath('bin/test.sh')
    --- drydock: end values ---
    Traceback (most recent call last):
      File "test-runner-posix-syntax.py", line 5, in <module>
        assert script.is_file()
               ^^^^^^^^^^^^^^^^
    AssertionError
- GREEN (prepassed): test-runner-covers-behaviors (FEATURE-TestRunner.md)
  intent: The test suite contains test modules for the add, list, remove, and rejection behaviors and pytest collects them without error.
  return code: 0
  stdout:
    tests/test_add_book.py::test_post_answers_201_with_stored_book_fields
    tests/test_add_book.py::test_post_response_body_carries_exactly_id_title_and_author
    tests/test_add_book.py::test_posted_book_reads_back_from_store
    tests/test_add_book.py::test_stored_title_and_author_keep_the_supplied_whitespace
    tests/test_add_book.py::test_two_books_added_in_sequence_receive_ascending_ids
    tests/test_app_shell.py::test_create_app_returns_flask_application
    tests/test_app_shell.py::test_create_app_opens_database_handle_for_services
    tests/test_app_shell.py::test_web_client_returns_test_client_in_testing_mode
    tests/test_app_shell.py::test_health_returns_200_with_status_body
    tests/test_app_shell.py::test_unknown_route_returns_404
    tests/test_app_shell.py::test_factory_registers_only_the_declared_routes
    tests/test_app_shell.py::test_base_layout_renders_title_block
    tests/test_app_shell.py::test_config_defaults_to_data_app_db
    tests/test_app_shell.py::test_config_prefers_database_url_over_database_path
    tests/test_app_shell.py::test_config_uses_database_path_when_url_absent
    tests/test_books_persistence.py::test_create_returns_stored_book_with_supplied_fields
    tests/test_books_persistence.py::test_create_assigns_distinct_ids
    tests/test_books_persistence.py::test_get_reads_back_created_book
    tests/test_books_persistence.py::test_get_returns_none_for_unknown_id
    tests/test_books_persistence.py::test_list_returns_books_in_order_added
    tests/test_books_persistence.py::test_delete_removes_book_from_next_list
    tests/test_books_persistence.py::test_created_book_is_visible_in_the_same_transaction
    tests/test_books_service.py::test_add_book_returns_stored_book_with_supplied_fields
    tests/test_books_service.py::test_add_book_persists_the_book
    tests/test_books_service.py::test_add_book_rejects_empty_title_without_storing
    tests/test_books_service.py::test_list_books_on_empty_store_returns_empty_list
    tests/test_books_service.py::test_list_books_returns_books_in_order_added
    tests/test_books_service.py::test_remove_book_returns_true_and_drops_book_from_list
    tests/test_books_service.py::test_remove_book_returns_false_for_unknown_id
    tests/test_books_service.py::test_remove_book_second_removal_returns_false
    tests/test_books_service.py::test_validate_book_input_accepts_non_blank_text[Dune-Frank Herbert]
    tests/test_books_service.py::test_validate_book_input_accepts_non_blank_text[  Dune  -  Frank Herbert  ]
    tests/test_books_service.py::test_validate_book_input_accepts_non_blank_text[T-A]
    tests/test_books_service.py::test_validate_book_input_names_the_offending_field[-A-title]
    tests/test_books_service.py::test_validate_book_input_names_the_offending_field[   -A-title]
    tests/test_books_service.py::test_validate_book_input_names_the_offending_field[None-A-title]
    tests/test_books_service.py::test_validate_book_input_names_the_offending_field[42-A-title]
    tests/test_books_service.py::test_validate_book_input_names_the_offending_field[T--author]
    tests/test_books_service.py::test_validate_book_input_names_the_offending_field[T-\t\n-author]
    tests/test_books_service.py::test_validate_book_input_names_the_offending_field[T-None-author]
    tests/test_books_service.py::test_validate_book_input_names_both_fields_when_both_are_blank
    tests/test_list_books.py::test_get_on_empty_store_answers_200_with_empty_array
    tests/test_list_books.py::test_list_returns_titles_in_the_order_they_were_added
    tests/test_list_books.py::test_list_returns_added_ids_in_submission_order
    tests/test_list_books.py::test_each_listed_book_carries_id_title_and_author
    tests/test_list_books.py::test_order_survives_reopening_the_store
    tests/test_project_foundation.py::test_declares_supported_python_version
    tests/test_project_foundation.py::test_runtime_dependencies_include_flask
    tests/test_project_foundation.py::test_dev_group_includes_pytest
    tests/test_project_foundation.py::test_lockfile_exists_at_root
    tests/test_project_foundation.py::test_tests_directory_and_conftest_exist
    tests/test_project_foundation.py::test_pytest_discovers_tests_from_project_root
    tests/test_project_foundation.py::test_running_interpreter_can_import_flask
    tests/test_project_foundation.py::test_python_runtime_meets_declared_minimum
    tests/test_reading_list_page.py::test_index_answers_200_with_html
    tests/test_reading_list_page.py::test_index_on_empty_store_shows_no_books_message
    tests/test_reading_list_page.py::test_index_with_books_does_not_show_empty_message
    tests/test_reading_list_page.py::test_index_lists_each_book_with_its_title_and_author
    tests/test_reading_list_page.py::test_index_lists_books_in_the_order_they_were_added
    tests/test_reading_list_page.py::test_index_escapes_book_text_so_markup_is_shown_literally
    tests/test_reading_list_page.py::test_index_on_plain_load_shows_no_error_region
    tests/test_reading_list_page.py::test_index_has_add_form_with_title_and_author_fields
    tests/test_reading_list_page.py::test_index_gives_each_book_a_remove_form_for_its_id
    tests/test_reading_list_page.py::test_index_uses_no_script_tags
    tests/test_reading_list_page.py::test_add_valid_book_answers_303_redirecting_to_index
    tests/test_reading_list_page.py::test_add_valid_book_stores_it_readable_through_the_list
    tests/test_reading_list_page.py::test_added_book_appears_at_the_end_of_the_page_list
    tests/test_reading_list_page.py::test_add_rejects_empty_or_missing_fields_with_400[form0]
    tests/test_reading_list_page.py::test_add_rejects_empty_or_missing_fields_with_400[form1]
    tests/test_reading_list_page.py::test_add_rejects_empty_or_missing_fields_with_400[form2]
    tests/test_reading_list_page.py::test_add_rejects_empty_or_missing_fields_with_400[form3]
    tests/test_reading_list_page.py::test_add_rejects_empty_or_missing_fields_with_400[form4]
    tests/test_reading_list_page.py::test_add_rejects_empty_or_missing_fields_with_400[form5]
    tests/test_reading_list_page.py::test_add_rejects_empty_or_missing_fields_with_400[form6]
    tests/test_reading_list_page.py::test_add_rejects_empty_or_missing_fields_with_400[form7]
    tests/test_reading_list_page.py::test_add_rejection_renders_visible_error_region
    tests/test_reading_list_page.py::test_add_rejection_stores_nothing
    tests/test_reading_list_page.py::test_add_rejection_leaves_the_list_unchanged_on_the_page
    tests/test_reading_list_page.py::test_add_rejection_echoes_entered_values_into_the_form
    tests/test_reading_list_page.py::test_add_rejection_does_not_show_an_error_on_the_next_plain_load
    tests/test_reading_list_page.py::test_remove_answers_303_redirecting_to_index
    tests/test_reading_list_page.py::test_removed_book_is_absent_from_the_page
    tests/test_reading_list_page.py::test_removed_book_is_absent_from_the_next_list_read
    tests/test_reading_list_page.py::test_removed_book_does_not_reappear_on_later_page_loads
    tests/test_reading_list_page.py::test_removing_a_middle_book_keeps_the_others_in_order
    tests/test_reading_list_page.py::test_removing_the_last_book_shows_the_empty_message
    tests/test_reading_list_page.py::test_removing_an_unknown_id_answers_303_redirecting_to_index
    tests/test_reading_list_page.py::test_removing_an_unknown_id_leaves_the_list_unchanged
    tests/test_reading_list_page.py::test_removing_the_same_book_twice_answers_303_both_times
    tests/test_reject_empty_fields.py::test_blank_or_missing_field_answers_400_with_error_message[payload0]
    tests/test_reject_empty_fields.py::test_blank_or_missing_field_answers_400_with_error_message[payload1]
    tests/test_reject_empty_fields.py::test_blank_or_missing_field_answers_400_with_error_message[payload2]
    tests/test_reject_empty_fields.py::test_blank_or_missing_field_answers_400_with_error_message[payload3]
    tests/test_reject_empty_fields.py::test_blank_or_missing_field_answers_400_with_error_message[payload4]
    tests/test_reject_empty_fields.py::test_blank_or_missing_field_answers_400_with_error_message[payload5]
    tests/test_reject_empty_fields.py::test_blank_or_missing_field_answers_400_with_error_message[payload6]
    tests/test_reject_empty_fields.py::test_blank_or_missing_field_answers_400_with_error_message[payload7]
    tests/test_reject_empty_fields.py::test_blank_or_missing_field_answers_400_with_error_message[payload8]
    tests/test_reject_empty_fields.py::test_error_names_the_offending_field[payload0-title]
    tests/test_reject_empty_fields.py::test_error_names_the_offending_field[payload1-author]
    tests/test_reject_empty_fields.py::test_non_json_body_answers_400
    tests/test_reject_empty_fields.py::test_rejected_submissions_store_nothing
    tests/test_remove_book.py::test_delete_answers_204_with_empty_body
    tests/test_remove_book.py::test_removed_book_is_absent_from_next_list_read
    tests/test_remove_book.py::test_removed_book_stays_absent_after_reopening_the_store
    tests/test_remove_book.py::test_remaining_books_keep_their_order_after_a_middle_removal
    tests/test_remove_book.py::test_removing_an_unknown_id_answers_404_with_error_body
    tests/test_remove_book.py::test_removing_the_same_id_twice_answers_404_the_second_time
    tests/test_remove_book.py::test_unknown_removal_leaves_the_list_unchanged
    tests/test_remove_book.py::test_non_integer_id_does_not_match_the_route
    
    110 tests collected in 0.26s
- RED: test-runner-full-suite (FEATURE-TestRunner.md)
  intent: The Commander-owned entry point sources/full_test.sh dispatches to bin/test.sh and the complete automated suite exits zero.
  return code: 1
  stdout:
    error: no bin/test.sh at the application root.
    st-001 requires the application to provide a POSIX-compatible bin/test.sh that exits
    zero when every automated test passes.
  stderr:
    --- drydock: values at failure ---
      result = CompletedProcess(args=['sh', 'sources/full_test.sh'], returncode=1, stdout='', stderr='error: no bin/test.sh at the application root.\nst-001 requires the application to provide a POSIX-compatible bin/test.sh that exits\nzero when every automated test passes.\n')
    --- drydock: end values ---
    Traceback (most recent call last):
      File "test-runner-full-suite.py", line 11, in <module>
        assert result.returncode == 0
               ^^^^^^^^^^^^^^^^^^^^^^
    AssertionError
- RED: test-runner-direct (FEATURE-TestRunner.md)
  intent: Running sh bin/test.sh from the application root exits zero.
  return code: 1
  stdout:
    sh: 0: cannot open bin/test.sh: No such file
  stderr:
    --- drydock: values at failure ---
      result = CompletedProcess(args=['sh', 'bin/test.sh'], returncode=2, stdout='', stderr='sh: 0: cannot open bin/test.sh: No such file\n')
    --- drydock: end values ---
    Traceback (most recent call last):
      File "test-runner-direct.py", line 11, in <module>
        assert result.returncode == 0
               ^^^^^^^^^^^^^^^^^^^^^^
    AssertionError

## Post-build programmatic acceptance
- PASS: test-runner-posix-syntax (FEATURE-TestRunner.md)
  intent: bin/test.sh exists and parses as POSIX sh without errors.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/uat/ReadingList/runs/20261023.174350/build/ReadingList/.venv/bin/python
  provisioning: not required
  return code: 0
- PASS: test-runner-covers-behaviors (FEATURE-TestRunner.md)
  intent: The test suite contains test modules for the add, list, remove, and rejection behaviors and pytest collects them without error.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/uat/ReadingList/runs/20261023.174350/build/ReadingList/.venv/bin/python
  provisioning: not required
  return code: 0
  stdout:
    tests/test_add_book.py::test_post_answers_201_with_stored_book_fields
    tests/test_add_book.py::test_post_response_body_carries_exactly_id_title_and_author
    tests/test_add_book.py::test_posted_book_reads_back_from_store
    tests/test_add_book.py::test_stored_title_and_author_keep_the_supplied_whitespace
    tests/test_add_book.py::test_two_books_added_in_sequence_receive_ascending_ids
    tests/test_app_shell.py::test_create_app_returns_flask_application
    tests/test_app_shell.py::test_create_app_opens_database_handle_for_services
    tests/test_app_shell.py::test_web_client_returns_test_client_in_testing_mode
    tests/test_app_shell.py::test_health_returns_200_with_status_body
    tests/test_app_shell.py::test_unknown_route_returns_404
    tests/test_app_shell.py::test_factory_registers_only_the_declared_routes
    tests/test_app_shell.py::test_base_layout_renders_title_block
    tests/test_app_shell.py::test_config_defaults_to_data_app_db
    tests/test_app_shell.py::test_config_prefers_database_url_over_database_path
    tests/test_app_shell.py::test_config_uses_database_path_when_url_absent
    tests/test_books_persistence.py::test_create_returns_stored_book_with_supplied_fields
    tests/test_books_persistence.py::test_create_assigns_distinct_ids
    tests/test_books_persistence.py::test_get_reads_back_created_book
    tests/test_books_persistence.py::test_get_returns_none_for_unknown_id
    tests/test_books_persistence.py::test_list_returns_books_in_order_added
    tests/test_books_persistence.py::test_delete_removes_book_from_next_list
    tests/test_books_persistence.py::test_created_book_is_visible_in_the_same_transaction
    tests/test_books_service.py::test_add_book_returns_stored_book_with_supplied_fields
    tests/test_books_service.py::test_add_book_persists_the_book
    tests/test_books_service.py::test_add_book_rejects_empty_title_without_storing
    tests/test_books_service.py::test_list_books_on_empty_store_returns_empty_list
    tests/test_books_service.py::test_list_books_returns_books_in_order_added
    tests/test_books_service.py::test_remove_book_returns_true_and_drops_book_from_list
    tests/test_books_service.py::test_remove_book_returns_false_for_unknown_id
    tests/test_books_service.py::test_remove_book_second_removal_returns_false
    tests/test_books_service.py::test_validate_book_input_accepts_non_blank_text[Dune-Frank Herbert]
    tests/test_books_service.py::test_validate_book_input_accepts_non_blank_text[  Dune  -  Frank Herbert  ]
    tests/test_books_service.py::test_validate_book_input_accepts_non_blank_text[T-A]
    tests/test_books_service.py::test_validate_book_input_names_the_offending_field[-A-title]
    tests/test_books_service.py::test_validate_book_input_names_the_offending_field[   -A-title]
    tests/test_books_service.py::test_validate_book_input_names_the_offending_field[None-A-title]
    tests/test_books_service.py::test_validate_book_input_names_the_offending_field[42-A-title]
    tests/test_books_service.py::test_validate_book_input_names_the_offending_field[T--author]
    tests/test_books_service.py::test_validate_book_input_names_the_offending_field[T-\t\n-author]
    tests/test_books_service.py::test_validate_book_input_names_the_offending_field[T-None-author]
    tests/test_books_service.py::test_validate_book_input_names_both_fields_when_both_are_blank
    tests/test_list_books.py::test_get_on_empty_store_answers_200_with_empty_array
    tests/test_list_books.py::test_list_returns_titles_in_the_order_they_were_added
    tests/test_list_books.py::test_list_returns_added_ids_in_submission_order
    tests/test_list_books.py::test_each_listed_book_carries_id_title_and_author
    tests/test_list_books.py::test_order_survives_reopening_the_store
    tests/test_project_foundation.py::test_declares_supported_python_version
    tests/test_project_foundation.py::test_runtime_dependencies_include_flask
    tests/test_project_foundation.py::test_dev_group_includes_pytest
    tests/test_project_foundation.py::test_lockfile_exists_at_root
    tests/test_project_foundation.py::test_tests_directory_and_conftest_exist
    tests/test_project_foundation.py::test_pytest_discovers_tests_from_project_root
    tests/test_project_foundation.py::test_running_interpreter_can_import_flask
    tests/test_project_foundation.py::test_python_runtime_meets_declared_minimum
    tests/test_reading_list_page.py::test_index_answers_200_with_html
    tests/test_reading_list_page.py::test_index_on_empty_store_shows_no_books_message
    tests/test_reading_list_page.py::test_index_with_books_does_not_show_empty_message
    tests/test_reading_list_page.py::test_index_lists_each_book_with_its_title_and_author
    tests/test_reading_list_page.py::test_index_lists_books_in_the_order_they_were_added
    tests/test_reading_list_page.py::test_index_escapes_book_text_so_markup_is_shown_literally
    tests/test_reading_list_page.py::test_index_on_plain_load_shows_no_error_region
    tests/test_reading_list_page.py::test_index_has_add_form_with_title_and_author_fields
    tests/test_reading_list_page.py::test_index_gives_each_book_a_remove_form_for_its_id
    tests/test_reading_list_page.py::test_index_uses_no_script_tags
    tests/test_reading_list_page.py::test_add_valid_book_answers_303_redirecting_to_index
    tests/test_reading_list_page.py::test_add_valid_book_stores_it_readable_through_the_list
    tests/test_reading_list_page.py::test_added_book_appears_at_the_end_of_the_page_list
    tests/test_reading_list_page.py::test_add_rejects_empty_or_missing_fields_with_400[form0]
    tests/test_reading_list_page.py::test_add_rejects_empty_or_missing_fields_with_400[form1]
    tests/test_reading_list_page.py::test_add_rejects_empty_or_missing_fields_with_400[form2]
    tests/test_reading_list_page.py::test_add_rejects_empty_or_missing_fields_with_400[form3]
    tests/test_reading_list_page.py::test_add_rejects_empty_or_missing_fields_with_400[form4]
    tests/test_reading_list_page.py::test_add_rejects_empty_or_missing_fields_with_400[form5]
    tests/test_reading_list_page.py::test_add_rejects_empty_or_missing_fields_with_400[form6]
    tests/test_reading_list_page.py::test_add_rejects_empty_or_missing_fields_with_400[form7]
    tests/test_reading_list_page.py::test_add_rejection_renders_visible_error_region
    tests/test_reading_list_page.py::test_add_rejection_stores_nothing
    tests/test_reading_list_page.py::test_add_rejection_leaves_the_list_unchanged_on_the_page
    tests/test_reading_list_page.py::test_add_rejection_echoes_entered_values_into_the_form
    tests/test_reading_list_page.py::test_add_rejection_does_not_show_an_error_on_the_next_plain_load
    tests/test_reading_list_page.py::test_remove_answers_303_redirecting_to_index
    tests/test_reading_list_page.py::test_removed_book_is_absent_from_the_page
    tests/test_reading_list_page.py::test_removed_book_is_absent_from_the_next_list_read
    tests/test_reading_list_page.py::test_removed_book_does_not_reappear_on_later_page_loads
    tests/test_reading_list_page.py::test_removing_a_middle_book_keeps_the_others_in_order
    tests/test_reading_list_page.py::test_removing_the_last_book_shows_the_empty_message
    tests/test_reading_list_page.py::test_removing_an_unknown_id_answers_303_redirecting_to_index
    tests/test_reading_list_page.py::test_removing_an_unknown_id_leaves_the_list_unchanged
    tests/test_reading_list_page.py::test_removing_the_same_book_twice_answers_303_both_times
    tests/test_reject_empty_fields.py::test_blank_or_missing_field_answers_400_with_error_message[payload0]
    tests/test_reject_empty_fields.py::test_blank_or_missing_field_answers_400_with_error_message[payload1]
    tests/test_reject_empty_fields.py::test_blank_or_missing_field_answers_400_with_error_message[payload2]
    tests/test_reject_empty_fields.py::test_blank_or_missing_field_answers_400_with_error_message[payload3]
    tests/test_reject_empty_fields.py::test_blank_or_missing_field_answers_400_with_error_message[payload4]
    tests/test_reject_empty_fields.py::test_blank_or_missing_field_answers_400_with_error_message[payload5]
    tests/test_reject_empty_fields.py::test_blank_or_missing_field_answers_400_with_error_message[payload6]
    tests/test_reject_empty_fields.py::test_blank_or_missing_field_answers_400_with_error_message[payload7]
    tests/test_reject_empty_fields.py::test_blank_or_missing_field_answers_400_with_error_message[payload8]
    tests/test_reject_empty_fields.py::test_error_names_the_offending_field[payload0-title]
    tests/test_reject_empty_fields.py::test_error_names_the_offending_field[payload1-author]
    tests/test_reject_empty_fields.py::test_non_json_body_answers_400
    tests/test_reject_empty_fields.py::test_rejected_submissions_store_nothing
    tests/test_remove_book.py::test_delete_answers_204_with_empty_body
    tests/test_remove_book.py::test_removed_book_is_absent_from_next_list_read
    tests/test_remove_book.py::test_removed_book_stays_absent_after_reopening_the_store
    tests/test_remove_book.py::test_remaining_books_keep_their_order_after_a_middle_removal
    tests/test_remove_book.py::test_removing_an_unknown_id_answers_404_with_error_body
    tests/test_remove_book.py::test_removing_the_same_id_twice_answers_404_the_second_time
    tests/test_remove_book.py::test_unknown_removal_leaves_the_list_unchanged
    tests/test_remove_book.py::test_non_integer_id_does_not_match_the_route
    tests/test_test_runner.py::test_runner_exits_zero_when_pytest_passes
    tests/test_test_runner.py::test_runner_passes_through_pytest_failure_status
    tests/test_test_runner.py::test_runner_passes_through_pytest_error_status
    tests/test_test_runner.py::test_runner_invokes_pytest_quietly
    tests/test_test_runner.py::test_runner_changes_to_app_root_from_another_directory
    tests/test_test_runner.py::test_runner_activates_venv_when_present
    tests/test_test_runner.py::test_runner_uses_path_pytest_when_venv_absent
    
    117 tests collected in 0.22s
- PASS: test-runner-full-suite (FEATURE-TestRunner.md)
  intent: The Commander-owned entry point sources/full_test.sh dispatches to bin/test.sh and the complete automated suite exits zero.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/uat/ReadingList/runs/20261023.174350/build/ReadingList/.venv/bin/python
  provisioning: not required
  return code: 0
  stdout:
    ........................................................................ [ 61%]
    .............................................                            [100%]
    117 passed in 2.50s
- PASS: test-runner-direct (FEATURE-TestRunner.md)
  intent: Running sh bin/test.sh from the application root exits zero.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/uat/ReadingList/runs/20261023.174350/build/ReadingList/.venv/bin/python
  provisioning: not required
  return code: 0
  stdout:
    ........................................................................ [ 61%]
    .............................................                            [100%]
    117 passed in 2.21s

## Build summary
I'll start by inspecting the build directory and the staged `sources/full_test.sh`.Existing tests from earlier blocks are present. I'll run the current suite to get a baseline before writing anything.Baseline is 110 passing. `bin/test.sh` doesn't exist yet. Next I'll check what the existing tests expect about `bin/` and confirm coverage for add, list, remove, and rejection.Coverage for add, list, removal, and rejection already exists (110 tests, all passing). The missing pieces are `bin/test.sh` and tests for the runner itself. I'll write the script to the spec: POSIX `sh`, `cd` to the application root, source `.venv` when present, run `pytest -q`, and return pytest's status unchanged.Next, tests for the runner. I'm avoiding a test that runs the real `bin/test.sh` from inside pytest, since that would recurse. Instead each test copies the real script into a temp application root and runs it with a stub `pytest` on `PATH`, then reads back the recorded state.Now I'll make the script executable, then run the declared checks: the syntax check, the collection check, `sh bin/test.sh`, and `sh sources/full_test.sh`. Each one's exit status is recorded.Both invocations exit zero and all 117 tests pass. But `set -u` makes `activate` emit an `OSTYPE: parameter not set` error under `sh`, so the run is noisy. The spec doesn't require `set -u`, so I'll remove it and rerun.The runner is done. `sh bin/test.sh` and `sh sources/full_test.sh` both exit 0 with 117 of 117 tests passing, and the runner also works from a different directory.

**Evidence (from this run):**
- `sh -n bin/test.sh`: exit 0
- `pytest --collect-only -q`: exit 0, 117 tests collected
- `sh bin/test.sh`: exit 0, `117 passed in 2.43s`
- `sh sources/full_test.sh`: exit 0, `117 passed in 2.70s`

The 110 existing tests from earlier blocks already cover adding, ordered listing, removal, and empty-field rejection. The 7 new runner tests cover pass-through of pytest's exit status (0, 3, 5), `-q`, working directory, and `.venv` activation.

<blueprint-decisions>
[{"spec":"FEATURE-TestRunner.md","severity":"Low","subject":"How bin/test.sh behavior is tested","decision":"The runner tests copy the real bin/test.sh into a temporary application root and run it with a stub pytest first on PATH. Running the real script from inside pytest would recurse. Is that acceptable?"}]
</blueprint-decisions>

RESULT: SUCCESS

FILES CHANGED:
- bin/test.sh
- tests/test_test_runner.py

SUMMARY:
`bin/test.sh` is a POSIX `sh` script. It resolves the application root from its own location, changes into it, sources `.venv/bin/activate` when that file exists, and runs `pytest -q` as its final command, so the script's exit status is pytest's. I left out `set -u` because it makes `activate` fail under `sh`. The script is also marked executable. `tests/test_test_runner.py` adds 7 tests that run a copy of the real script against a stub pytest and read back the recorded state. Verification counts: 117 collected, 117 passed, 0 failed, across the two invocations above. The `/tmp` files written during checks are scratch outside the build directory.

BLOCKERS:
- None.
