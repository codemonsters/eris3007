@tool
extends EditorPlugin


const MainPanel = preload("res://addons/DialogGenerator/DialogMenu.tscn")

var main_panel_instance
var dialog


func _enter_tree():
	dialog = read_json()
	print(dialog)
	main_panel_instance = MainPanel.instantiate()
	# Add the main panel to the editor's main viewport.
	get_editor_interface().get_editor_main_screen().add_child(main_panel_instance)
	# Hide the main panel. Very much required.
	_make_visible(false)


func _exit_tree():
	if main_panel_instance:
		main_panel_instance.queue_free()


func _has_main_screen():
	return true


func _make_visible(visible):
	if main_panel_instance:
		main_panel_instance.visible = visible


func _get_plugin_name():
	return "Dialog Editor"


func _get_plugin_icon():
	return get_editor_interface().get_base_control().get_theme_icon("Node", "EditorIcons")


func read_json():
	var dialogs = FileAccess.open("res://assets/dialog-sample.json", FileAccess.READ)
	var json_object = JSON.new()
	var parse_err = json_object.parse(dialogs.get_as_text())
	return json_object.get_data()
