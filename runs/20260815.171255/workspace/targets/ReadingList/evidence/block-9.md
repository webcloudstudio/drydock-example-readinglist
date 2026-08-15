# Evidence: Block 9 · Service (block-9)

- block type: block
- date: 2026-08-15
- resulting state: closed/verified
- story points (combined assembled cost): 3247
- execution id: 20260815.173420.972Z-2fbc3425

## Stories built
- Run and verify the complete automated test suite through bin/test.sh. (verification-suite) [story]

## Acceptance tooling authorization
- FEATURE-Test-Suite.md#complete-suite: executable=sh; scope=test; authorization=existing Target environment
- FEATURE-Test-Suite.md#launcher-runs-from-root: executable=sh; scope=test; authorization=existing Target environment
- FEATURE-Test-Suite.md#behavior-suite-command-exists: executable=sh; scope=test; authorization=existing Target environment

## Stacked context
- compass: COMPASS.md (SP 724)
- implements: FEATURE-Test-Suite.md (SP 609)
- context: ARCHITECTURE_compact.md (SP 133)
- context: DATABASE_compact.md (SP 164)
- stack: python_compact.md (SP 1534)

## Build directory changes
- bin/test.sh
- tests/test_launcher.py

## Pre-build acceptance observation
- GREEN (prepassed): complete-suite (FEATURE-Test-Suite.md)
  intent: The required POSIX test launcher runs the complete automated suite successfully.
  return code: 0
  stdout:
    ============================= test session starts ==============================
    platform linux -- Python 3.12.13, pytest-9.1.1, pluggy-1.6.0 -- /mnt/c/Users/barlo/projects/drydock/uat/ReadingList/runs/20260815.171255/build/ReadingList/.venv/bin/python
    cachedir: .pytest_cache
    rootdir: /mnt/c/Users/barlo/projects/drydock/uat/ReadingList/runs/20260815.171255/build/ReadingList
    configfile: pytest.ini
    collecting ... collected 36 items
    
    tests/test_architecture.py::test_factory_creates_runnable_application PASSED [  2%]
    tests/test_architecture.py::test_factory_isolates_application_instances PASSED [  5%]
    tests/test_architecture.py::test_testing_factory_uses_isolated_database_by_default PASSED [  8%]
    tests/test_architecture.py::test_app_module_exposes_factory_without_starting_server PASSED [ 11%]
    tests/test_ordered_list.py::test_root_is_successful_for_an_empty_store PASSED [ 13%]
    tests/test_ordered_list.py::test_empty_store_has_an_understandable_empty_state PASSED [ 16%]
    tests/test_ordered_list.py::test_root_renders_books_in_insertion_order PASSED [ 19%]
    tests/test_persistence.py::test_add_reads_back_submitted_book PASSED     [ 22%]
    tests/test_persistence.py::test_list_ordered_preserves_addition_order PASSED [ 25%]
    tests/test_persistence.py::test_remove_existing_book_removes_it PASSED   [ 27%]
    tests/test_persistence.py::test_new_database_lists_no_books PASSED       [ 30%]
    tests/test_persistence.py::test_add_rejects_empty_fields[-Author] PASSED [ 33%]
    tests/test_persistence.py::test_add_rejects_empty_fields[Title-] PASSED  [ 36%]
    tests/test_persistence.py::test_remove_missing_book_reports_false PASSED [ 38%]
    tests/test_persistence.py::test_initialization_is_idempotent_and_keeps_rows PASSED [ 41%]
    tests/test_persistence.py::test_database_rejects_null_book_fields PASSED [ 44%]
    tests/test_routes.py::test_root_renders_empty_list PASSED                [ 47%]
    tests/test_routes.py::test_reading_list_has_labeled_book_form_and_empty_state PASSED [ 50%]
    tests/test_routes.py::test_added_book_is_rendered_with_named_removal_control PASSED [ 52%]
    tests/test_routes.py::test_book_creation_redirects_to_the_list PASSED    [ 55%]
    tests/test_routes.py::test_book_creation_preserves_existing_insertion_order PASSED [ 58%]
    tests/test_routes.py::test_invalid_submission_keeps_reader_on_page_with_error PASSED [ 61%]
    tests/test_routes.py::test_invalid_submission_with_missing_author_returns_client_error PASSED [ 63%]
    tests/test_routes.py::test_submission_with_both_required_fields_missing_returns_client_error PASSED [ 66%]
    tests/test_routes.py::test_invalid_submission_is_not_persisted[Rejected Title-] PASSED [ 69%]
    tests/test_routes.py::test_invalid_submission_is_not_persisted[-Rejected Author] PASSED [ 72%]
    tests/test_routes.py::test_invalid_submission_is_not_persisted[-] PASSED [ 75%]
    tests/test_routes.py::test_valid_submission_remains_supported_after_validation PASSED [ 77%]
    tests/test_routes.py::test_removal_control_removes_only_target_book PASSED [ 80%]
    tests/test_routes.py::test_removal_route_preserves_relative_order_of_remaining_books PASSED [ 83%]
    tests/test_routes.py::test_removal_route_with_unknown_id_keeps_all_books PASSED [ 86%]
    tests/test_routes.py::test_health_reports_ok PASSED                      [ 88%]
    tests/test_screen.py::test_screen_loads_at_root PASSED                   [ 91%]
    tests/test_screen.py::test_screen_accepts_book_submission PASSED         [ 94%]
    tests/test_screen.py::test_screen_removes_book_using_its_identity PASSED [ 97%]
    tests/test_screen.py::test_screen_supports_an_empty_list PASSED          [100%]
    
    ============================== 36 passed in 0.81s ==============================
    
    warning: `VIRTUAL_ENV=/mnt/c/Users/barlo/projects/drydock/.venv` does not match the project environment path `.venv` and will be ignored; use `--active` to target the active environment instead
- GREEN (prepassed): launcher-runs-from-root (FEATURE-Test-Suite.md)
  intent: The test launcher is runnable from the application root using the required command.
  return code: 0
  stdout:
    ============================= test session starts ==============================
    platform linux -- Python 3.12.13, pytest-9.1.1, pluggy-1.6.0 -- /mnt/c/Users/barlo/projects/drydock/uat/ReadingList/runs/20260815.171255/build/ReadingList/.venv/bin/python
    cachedir: .pytest_cache
    rootdir: /mnt/c/Users/barlo/projects/drydock/uat/ReadingList/runs/20260815.171255/build/ReadingList
    configfile: pytest.ini
    collecting ... collected 36 items
    
    tests/test_architecture.py::test_factory_creates_runnable_application PASSED [  2%]
    tests/test_architecture.py::test_factory_isolates_application_instances PASSED [  5%]
    tests/test_architecture.py::test_testing_factory_uses_isolated_database_by_default PASSED [  8%]
    tests/test_architecture.py::test_app_module_exposes_factory_without_starting_server PASSED [ 11%]
    tests/test_ordered_list.py::test_root_is_successful_for_an_empty_store PASSED [ 13%]
    tests/test_ordered_list.py::test_empty_store_has_an_understandable_empty_state PASSED [ 16%]
    tests/test_ordered_list.py::test_root_renders_books_in_insertion_order PASSED [ 19%]
    tests/test_persistence.py::test_add_reads_back_submitted_book PASSED     [ 22%]
    tests/test_persistence.py::test_list_ordered_preserves_addition_order PASSED [ 25%]
    tests/test_persistence.py::test_remove_existing_book_removes_it PASSED   [ 27%]
    tests/test_persistence.py::test_new_database_lists_no_books PASSED       [ 30%]
    tests/test_persistence.py::test_add_rejects_empty_fields[-Author] PASSED [ 33%]
    tests/test_persistence.py::test_add_rejects_empty_fields[Title-] PASSED  [ 36%]
    tests/test_persistence.py::test_remove_missing_book_reports_false PASSED [ 38%]
    tests/test_persistence.py::test_initialization_is_idempotent_and_keeps_rows PASSED [ 41%]
    tests/test_persistence.py::test_database_rejects_null_book_fields PASSED [ 44%]
    tests/test_routes.py::test_root_renders_empty_list PASSED                [ 47%]
    tests/test_routes.py::test_reading_list_has_labeled_book_form_and_empty_state PASSED [ 50%]
    tests/test_routes.py::test_added_book_is_rendered_with_named_removal_control PASSED [ 52%]
    tests/test_routes.py::test_book_creation_redirects_to_the_list PASSED    [ 55%]
    tests/test_routes.py::test_book_creation_preserves_existing_insertion_order PASSED [ 58%]
    tests/test_routes.py::test_invalid_submission_keeps_reader_on_page_with_error PASSED [ 61%]
    tests/test_routes.py::test_invalid_submission_with_missing_author_returns_client_error PASSED [ 63%]
    tests/test_routes.py::test_submission_with_both_required_fields_missing_returns_client_error PASSED [ 66%]
    tests/test_routes.py::test_invalid_submission_is_not_persisted[Rejected Title-] PASSED [ 69%]
    tests/test_routes.py::test_invalid_submission_is_not_persisted[-Rejected Author] PASSED [ 72%]
    tests/test_routes.py::test_invalid_submission_is_not_persisted[-] PASSED [ 75%]
    tests/test_routes.py::test_valid_submission_remains_supported_after_validation PASSED [ 77%]
    tests/test_routes.py::test_removal_control_removes_only_target_book PASSED [ 80%]
    tests/test_routes.py::test_removal_route_preserves_relative_order_of_remaining_books PASSED [ 83%]
    tests/test_routes.py::test_removal_route_with_unknown_id_keeps_all_books PASSED [ 86%]
    tests/test_routes.py::test_health_reports_ok PASSED                      [ 88%]
    tests/test_screen.py::test_screen_loads_at_root PASSED                   [ 91%]
    tests/test_screen.py::test_screen_accepts_book_submission PASSED         [ 94%]
    tests/test_screen.py::test_screen_removes_book_using_its_identity PASSED [ 97%]
    tests/test_screen.py::test_screen_supports_an_empty_list PASSED          [100%]
    
    ============================== 36 passed in 0.85s ==============================
    
    warning: `VIRTUAL_ENV=/mnt/c/Users/barlo/projects/drydock/.venv` does not match the project environment path `.venv` and will be ignored; use `--active` to target the active environment instead
- GREEN (prepassed): behavior-suite-command-exists (FEATURE-Test-Suite.md)
  intent: The complete launcher invocation is the executable project verification boundary.
  return code: 0
  stdout:
    ============================= test session starts ==============================
    platform linux -- Python 3.12.13, pytest-9.1.1, pluggy-1.6.0 -- /mnt/c/Users/barlo/projects/drydock/uat/ReadingList/runs/20260815.171255/build/ReadingList/.venv/bin/python
    cachedir: .pytest_cache
    rootdir: /mnt/c/Users/barlo/projects/drydock/uat/ReadingList/runs/20260815.171255/build/ReadingList
    configfile: pytest.ini
    collecting ... collected 36 items
    
    tests/test_architecture.py::test_factory_creates_runnable_application PASSED [  2%]
    tests/test_architecture.py::test_factory_isolates_application_instances PASSED [  5%]
    tests/test_architecture.py::test_testing_factory_uses_isolated_database_by_default PASSED [  8%]
    tests/test_architecture.py::test_app_module_exposes_factory_without_starting_server PASSED [ 11%]
    tests/test_ordered_list.py::test_root_is_successful_for_an_empty_store PASSED [ 13%]
    tests/test_ordered_list.py::test_empty_store_has_an_understandable_empty_state PASSED [ 16%]
    tests/test_ordered_list.py::test_root_renders_books_in_insertion_order PASSED [ 19%]
    tests/test_persistence.py::test_add_reads_back_submitted_book PASSED     [ 22%]
    tests/test_persistence.py::test_list_ordered_preserves_addition_order PASSED [ 25%]
    tests/test_persistence.py::test_remove_existing_book_removes_it PASSED   [ 27%]
    tests/test_persistence.py::test_new_database_lists_no_books PASSED       [ 30%]
    tests/test_persistence.py::test_add_rejects_empty_fields[-Author] PASSED [ 33%]
    tests/test_persistence.py::test_add_rejects_empty_fields[Title-] PASSED  [ 36%]
    tests/test_persistence.py::test_remove_missing_book_reports_false PASSED [ 38%]
    tests/test_persistence.py::test_initialization_is_idempotent_and_keeps_rows PASSED [ 41%]
    tests/test_persistence.py::test_database_rejects_null_book_fields PASSED [ 44%]
    tests/test_routes.py::test_root_renders_empty_list PASSED                [ 47%]
    tests/test_routes.py::test_reading_list_has_labeled_book_form_and_empty_state PASSED [ 50%]
    tests/test_routes.py::test_added_book_is_rendered_with_named_removal_control PASSED [ 52%]
    tests/test_routes.py::test_book_creation_redirects_to_the_list PASSED    [ 55%]
    tests/test_routes.py::test_book_creation_preserves_existing_insertion_order PASSED [ 58%]
    tests/test_routes.py::test_invalid_submission_keeps_reader_on_page_with_error PASSED [ 61%]
    tests/test_routes.py::test_invalid_submission_with_missing_author_returns_client_error PASSED [ 63%]
    tests/test_routes.py::test_submission_with_both_required_fields_missing_returns_client_error PASSED [ 66%]
    tests/test_routes.py::test_invalid_submission_is_not_persisted[Rejected Title-] PASSED [ 69%]
    tests/test_routes.py::test_invalid_submission_is_not_persisted[-Rejected Author] PASSED [ 72%]
    tests/test_routes.py::test_invalid_submission_is_not_persisted[-] PASSED [ 75%]
    tests/test_routes.py::test_valid_submission_remains_supported_after_validation PASSED [ 77%]
    tests/test_routes.py::test_removal_control_removes_only_target_book PASSED [ 80%]
    tests/test_routes.py::test_removal_route_preserves_relative_order_of_remaining_books PASSED [ 83%]
    tests/test_routes.py::test_removal_route_with_unknown_id_keeps_all_books PASSED [ 86%]
    tests/test_routes.py::test_health_reports_ok PASSED                      [ 88%]
    tests/test_screen.py::test_screen_loads_at_root PASSED                   [ 91%]
    tests/test_screen.py::test_screen_accepts_book_submission PASSED         [ 94%]
    tests/test_screen.py::test_screen_removes_book_using_its_identity PASSED [ 97%]
    tests/test_screen.py::test_screen_supports_an_empty_list PASSED          [100%]
    
    ============================== 36 passed in 0.86s ==============================
    
    warning: `VIRTUAL_ENV=/mnt/c/Users/barlo/projects/drydock/.venv` does not match the project environment path `.venv` and will be ignored; use `--active` to target the active environment instead

## Post-build programmatic acceptance
- PASS: complete-suite (FEATURE-Test-Suite.md)
  intent: The required POSIX test launcher runs the complete automated suite successfully.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/uat/ReadingList/runs/20260815.171255/build/ReadingList/.venv/bin/python
  provisioning: not required
  return code: 0
  stdout:
    ============================= test session starts ==============================
    platform linux -- Python 3.12.13, pytest-9.1.1, pluggy-1.6.0 -- /mnt/c/Users/barlo/projects/drydock/uat/ReadingList/runs/20260815.171255/build/ReadingList/.venv/bin/python
    cachedir: .pytest_cache
    rootdir: /mnt/c/Users/barlo/projects/drydock/uat/ReadingList/runs/20260815.171255/build/ReadingList
    configfile: pytest.ini
    collecting ... collected 38 items
    
    tests/test_architecture.py::test_factory_creates_runnable_application PASSED [  2%]
    tests/test_architecture.py::test_factory_isolates_application_instances PASSED [  5%]
    tests/test_architecture.py::test_testing_factory_uses_isolated_database_by_default PASSED [  7%]
    tests/test_architecture.py::test_app_module_exposes_factory_without_starting_server PASSED [ 10%]
    tests/test_launcher.py::test_test_launcher_has_valid_posix_syntax PASSED [ 13%]
    tests/test_launcher.py::test_test_launcher_runs_pytest_from_project_root PASSED [ 15%]
    tests/test_ordered_list.py::test_root_is_successful_for_an_empty_store PASSED [ 18%]
    tests/test_ordered_list.py::test_empty_store_has_an_understandable_empty_state PASSED [ 21%]
    tests/test_ordered_list.py::test_root_renders_books_in_insertion_order PASSED [ 23%]
    tests/test_persistence.py::test_add_reads_back_submitted_book PASSED     [ 26%]
    tests/test_persistence.py::test_list_ordered_preserves_addition_order PASSED [ 28%]
    tests/test_persistence.py::test_remove_existing_book_removes_it PASSED   [ 31%]
    tests/test_persistence.py::test_new_database_lists_no_books PASSED       [ 34%]
    tests/test_persistence.py::test_add_rejects_empty_fields[-Author] PASSED [ 36%]
    tests/test_persistence.py::test_add_rejects_empty_fields[Title-] PASSED  [ 39%]
    tests/test_persistence.py::test_remove_missing_book_reports_false PASSED [ 42%]
    tests/test_persistence.py::test_initialization_is_idempotent_and_keeps_rows PASSED [ 44%]
    tests/test_persistence.py::test_database_rejects_null_book_fields PASSED [ 47%]
    tests/test_routes.py::test_root_renders_empty_list PASSED                [ 50%]
    tests/test_routes.py::test_reading_list_has_labeled_book_form_and_empty_state PASSED [ 52%]
    tests/test_routes.py::test_added_book_is_rendered_with_named_removal_control PASSED [ 55%]
    tests/test_routes.py::test_book_creation_redirects_to_the_list PASSED    [ 57%]
    tests/test_routes.py::test_book_creation_preserves_existing_insertion_order PASSED [ 60%]
    tests/test_routes.py::test_invalid_submission_keeps_reader_on_page_with_error PASSED [ 63%]
    tests/test_routes.py::test_invalid_submission_with_missing_author_returns_client_error PASSED [ 65%]
    tests/test_routes.py::test_submission_with_both_required_fields_missing_returns_client_error PASSED [ 68%]
    tests/test_routes.py::test_invalid_submission_is_not_persisted[Rejected Title-] PASSED [ 71%]
    tests/test_routes.py::test_invalid_submission_is_not_persisted[-Rejected Author] PASSED [ 73%]
    tests/test_routes.py::test_invalid_submission_is_not_persisted[-] PASSED [ 76%]
    tests/test_routes.py::test_valid_submission_remains_supported_after_validation PASSED [ 78%]
    tests/test_routes.py::test_removal_control_removes_only_target_book PASSED [ 81%]
    tests/test_routes.py::test_removal_route_preserves_relative_order_of_remaining_books PASSED [ 84%]
    tests/test_routes.py::test_removal_route_with_unknown_id_keeps_all_books PASSED [ 86%]
    tests/test_routes.py::test_health_reports_ok PASSED                      [ 89%]
    tests/test_screen.py::test_screen_loads_at_root PASSED                   [ 92%]
    tests/test_screen.py::test_screen_accepts_book_submission PASSED         [ 94%]
    tests/test_screen.py::test_screen_removes_book_using_its_identity PASSED [ 97%]
    tests/test_screen.py::test_screen_supports_an_empty_list PASSED          [100%]
    
    ============================== 38 passed in 0.99s ==============================
    
    warning: `VIRTUAL_ENV=/mnt/c/Users/barlo/projects/drydock/.venv` does not match the project environment path `.venv` and will be ignored; use `--active` to target the active environment instead
- PASS: launcher-runs-from-root (FEATURE-Test-Suite.md)
  intent: The test launcher is runnable from the application root using the required command.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/uat/ReadingList/runs/20260815.171255/build/ReadingList/.venv/bin/python
  provisioning: not required
  return code: 0
  stdout:
    ============================= test session starts ==============================
    platform linux -- Python 3.12.13, pytest-9.1.1, pluggy-1.6.0 -- /mnt/c/Users/barlo/projects/drydock/uat/ReadingList/runs/20260815.171255/build/ReadingList/.venv/bin/python
    cachedir: .pytest_cache
    rootdir: /mnt/c/Users/barlo/projects/drydock/uat/ReadingList/runs/20260815.171255/build/ReadingList
    configfile: pytest.ini
    collecting ... collected 38 items
    
    tests/test_architecture.py::test_factory_creates_runnable_application PASSED [  2%]
    tests/test_architecture.py::test_factory_isolates_application_instances PASSED [  5%]
    tests/test_architecture.py::test_testing_factory_uses_isolated_database_by_default PASSED [  7%]
    tests/test_architecture.py::test_app_module_exposes_factory_without_starting_server PASSED [ 10%]
    tests/test_launcher.py::test_test_launcher_has_valid_posix_syntax PASSED [ 13%]
    tests/test_launcher.py::test_test_launcher_runs_pytest_from_project_root PASSED [ 15%]
    tests/test_ordered_list.py::test_root_is_successful_for_an_empty_store PASSED [ 18%]
    tests/test_ordered_list.py::test_empty_store_has_an_understandable_empty_state PASSED [ 21%]
    tests/test_ordered_list.py::test_root_renders_books_in_insertion_order PASSED [ 23%]
    tests/test_persistence.py::test_add_reads_back_submitted_book PASSED     [ 26%]
    tests/test_persistence.py::test_list_ordered_preserves_addition_order PASSED [ 28%]
    tests/test_persistence.py::test_remove_existing_book_removes_it PASSED   [ 31%]
    tests/test_persistence.py::test_new_database_lists_no_books PASSED       [ 34%]
    tests/test_persistence.py::test_add_rejects_empty_fields[-Author] PASSED [ 36%]
    tests/test_persistence.py::test_add_rejects_empty_fields[Title-] PASSED  [ 39%]
    tests/test_persistence.py::test_remove_missing_book_reports_false PASSED [ 42%]
    tests/test_persistence.py::test_initialization_is_idempotent_and_keeps_rows PASSED [ 44%]
    tests/test_persistence.py::test_database_rejects_null_book_fields PASSED [ 47%]
    tests/test_routes.py::test_root_renders_empty_list PASSED                [ 50%]
    tests/test_routes.py::test_reading_list_has_labeled_book_form_and_empty_state PASSED [ 52%]
    tests/test_routes.py::test_added_book_is_rendered_with_named_removal_control PASSED [ 55%]
    tests/test_routes.py::test_book_creation_redirects_to_the_list PASSED    [ 57%]
    tests/test_routes.py::test_book_creation_preserves_existing_insertion_order PASSED [ 60%]
    tests/test_routes.py::test_invalid_submission_keeps_reader_on_page_with_error PASSED [ 63%]
    tests/test_routes.py::test_invalid_submission_with_missing_author_returns_client_error PASSED [ 65%]
    tests/test_routes.py::test_submission_with_both_required_fields_missing_returns_client_error PASSED [ 68%]
    tests/test_routes.py::test_invalid_submission_is_not_persisted[Rejected Title-] PASSED [ 71%]
    tests/test_routes.py::test_invalid_submission_is_not_persisted[-Rejected Author] PASSED [ 73%]
    tests/test_routes.py::test_invalid_submission_is_not_persisted[-] PASSED [ 76%]
    tests/test_routes.py::test_valid_submission_remains_supported_after_validation PASSED [ 78%]
    tests/test_routes.py::test_removal_control_removes_only_target_book PASSED [ 81%]
    tests/test_routes.py::test_removal_route_preserves_relative_order_of_remaining_books PASSED [ 84%]
    tests/test_routes.py::test_removal_route_with_unknown_id_keeps_all_books PASSED [ 86%]
    tests/test_routes.py::test_health_reports_ok PASSED                      [ 89%]
    tests/test_screen.py::test_screen_loads_at_root PASSED                   [ 92%]
    tests/test_screen.py::test_screen_accepts_book_submission PASSED         [ 94%]
    tests/test_screen.py::test_screen_removes_book_using_its_identity PASSED [ 97%]
    tests/test_screen.py::test_screen_supports_an_empty_list PASSED          [100%]
    
    ============================== 38 passed in 0.95s ==============================
    
    warning: `VIRTUAL_ENV=/mnt/c/Users/barlo/projects/drydock/.venv` does not match the project environment path `.venv` and will be ignored; use `--active` to target the active environment instead
- PASS: behavior-suite-command-exists (FEATURE-Test-Suite.md)
  intent: The complete launcher invocation is the executable project verification boundary.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/uat/ReadingList/runs/20260815.171255/build/ReadingList/.venv/bin/python
  provisioning: not required
  return code: 0
  stdout:
    ============================= test session starts ==============================
    platform linux -- Python 3.12.13, pytest-9.1.1, pluggy-1.6.0 -- /mnt/c/Users/barlo/projects/drydock/uat/ReadingList/runs/20260815.171255/build/ReadingList/.venv/bin/python
    cachedir: .pytest_cache
    rootdir: /mnt/c/Users/barlo/projects/drydock/uat/ReadingList/runs/20260815.171255/build/ReadingList
    configfile: pytest.ini
    collecting ... collected 38 items
    
    tests/test_architecture.py::test_factory_creates_runnable_application PASSED [  2%]
    tests/test_architecture.py::test_factory_isolates_application_instances PASSED [  5%]
    tests/test_architecture.py::test_testing_factory_uses_isolated_database_by_default PASSED [  7%]
    tests/test_architecture.py::test_app_module_exposes_factory_without_starting_server PASSED [ 10%]
    tests/test_launcher.py::test_test_launcher_has_valid_posix_syntax PASSED [ 13%]
    tests/test_launcher.py::test_test_launcher_runs_pytest_from_project_root PASSED [ 15%]
    tests/test_ordered_list.py::test_root_is_successful_for_an_empty_store PASSED [ 18%]
    tests/test_ordered_list.py::test_empty_store_has_an_understandable_empty_state PASSED [ 21%]
    tests/test_ordered_list.py::test_root_renders_books_in_insertion_order PASSED [ 23%]
    tests/test_persistence.py::test_add_reads_back_submitted_book PASSED     [ 26%]
    tests/test_persistence.py::test_list_ordered_preserves_addition_order PASSED [ 28%]
    tests/test_persistence.py::test_remove_existing_book_removes_it PASSED   [ 31%]
    tests/test_persistence.py::test_new_database_lists_no_books PASSED       [ 34%]
    tests/test_persistence.py::test_add_rejects_empty_fields[-Author] PASSED [ 36%]
    tests/test_persistence.py::test_add_rejects_empty_fields[Title-] PASSED  [ 39%]
    tests/test_persistence.py::test_remove_missing_book_reports_false PASSED [ 42%]
    tests/test_persistence.py::test_initialization_is_idempotent_and_keeps_rows PASSED [ 44%]
    tests/test_persistence.py::test_database_rejects_null_book_fields PASSED [ 47%]
    tests/test_routes.py::test_root_renders_empty_list PASSED                [ 50%]
    tests/test_routes.py::test_reading_list_has_labeled_book_form_and_empty_state PASSED [ 52%]
    tests/test_routes.py::test_added_book_is_rendered_with_named_removal_control PASSED [ 55%]
    tests/test_routes.py::test_book_creation_redirects_to_the_list PASSED    [ 57%]
    tests/test_routes.py::test_book_creation_preserves_existing_insertion_order PASSED [ 60%]
    tests/test_routes.py::test_invalid_submission_keeps_reader_on_page_with_error PASSED [ 63%]
    tests/test_routes.py::test_invalid_submission_with_missing_author_returns_client_error PASSED [ 65%]
    tests/test_routes.py::test_submission_with_both_required_fields_missing_returns_client_error PASSED [ 68%]
    tests/test_routes.py::test_invalid_submission_is_not_persisted[Rejected Title-] PASSED [ 71%]
    tests/test_routes.py::test_invalid_submission_is_not_persisted[-Rejected Author] PASSED [ 73%]
    tests/test_routes.py::test_invalid_submission_is_not_persisted[-] PASSED [ 76%]
    tests/test_routes.py::test_valid_submission_remains_supported_after_validation PASSED [ 78%]
    tests/test_routes.py::test_removal_control_removes_only_target_book PASSED [ 81%]
    tests/test_routes.py::test_removal_route_preserves_relative_order_of_remaining_books PASSED [ 84%]
    tests/test_routes.py::test_removal_route_with_unknown_id_keeps_all_books PASSED [ 86%]
    tests/test_routes.py::test_health_reports_ok PASSED                      [ 89%]
    tests/test_screen.py::test_screen_loads_at_root PASSED                   [ 92%]
    tests/test_screen.py::test_screen_accepts_book_submission PASSED         [ 94%]
    tests/test_screen.py::test_screen_removes_book_using_its_identity PASSED [ 97%]
    tests/test_screen.py::test_screen_supports_an_empty_list PASSED          [100%]
    
    ============================== 38 passed in 0.91s ==============================
    
    warning: `VIRTUAL_ENV=/mnt/c/Users/barlo/projects/drydock/.venv` does not match the project environment path `.venv` and will be ignored; use `--active` to target the active environment instead

## Build summary
RESULT: SUCCESS

FILES CHANGED:
- bin/test.sh
- tests/test_launcher.py

SUMMARY:
Added launcher verification coverage. `sh bin/test.sh` passed all 38 tests with exit code 0; Ruff also passed.

BLOCKERS:
- None. `sources/` was absent.
