"""
Test suite for the Pink Morsel Sales Dashboard (Dash app).
Verifies that the dashboard contains expected components:
- Header with title
- Interactive visualization (chart)
- Region picker (radio buttons)
"""

import pytest
from dash import dcc, html
from app import app


class TestDashAppComponents:
    """Test suite for Dash app component presence and functionality."""
    
    def test_header_is_present(self):
        """
        Test that the header is present in the app layout.
        Verifies the H1 element with title 'Pink Morsel Sales Dashboard' exists.
        """
        # Get the app layout
        layout = app.layout
        
        # The layout is a Div containing Header, main content, and Footer
        # We need to find the Header element
        assert layout is not None, "App layout should not be None"
        
        # Check that layout has children
        assert hasattr(layout, 'children'), "Layout should have children"
        assert layout.children is not None, "Layout children should not be None"
        
        # Find the Header element (first child should be the header)
        header = layout.children[0]
        assert isinstance(header, html.Header), "First child should be a Header element"
        
        # Header should contain children
        assert hasattr(header, 'children'), "Header should have children"
        assert header.children is not None, "Header children should not be None"
        
        # Find the H1 element in the header
        h1_found = False
        h1_text = None
        
        for child in header.children:
            if isinstance(child, html.H1):
                h1_found = True
                # Get the text content from H1
                if hasattr(child, 'children'):
                    h1_text = child.children
                break
        
        assert h1_found, "Header should contain an H1 element"
        assert h1_text is not None, "H1 element should have text content"
        assert "Pink Morsel" in str(h1_text), "H1 should contain 'Pink Morsel' in title"
    
    def test_visualization_is_present(self):
        """
        Test that the visualization (dcc.Graph component) is present.
        Verifies that a Graph component exists in the app layout.
        """
        layout = app.layout
        
        assert layout is not None, "App layout should not be None"
        assert hasattr(layout, 'children'), "Layout should have children"
        
        # The main content is wrapped in a Div at layout.children[1]
        main_container = layout.children[1]
        assert isinstance(main_container, html.Div), "Main container should be a Div"
        
        # Look for the Graph component in the layout
        graph_found = False
        
        def find_graph(element):
            """Recursively search for a Graph component."""
            if isinstance(element, dcc.Graph):
                return True
            
            if hasattr(element, 'children') and element.children is not None:
                if isinstance(element.children, list):
                    for child in element.children:
                        if find_graph(child):
                            return True
                else:
                    if find_graph(element.children):
                        return True
            
            return False
        
        graph_found = find_graph(main_container)
        assert graph_found, "App layout should contain a dcc.Graph component for visualization"
    
    def test_region_picker_is_present(self):
        """
        Test that the region picker (dcc.RadioItems) is present with correct options.
        Verifies radio buttons for region filtering exist with all 5 options.
        """
        layout = app.layout
        
        assert layout is not None, "App layout should not be None"
        assert hasattr(layout, 'children'), "Layout should have children"
        
        # The main content is wrapped in a Div at layout.children[1]
        main_container = layout.children[1]
        assert isinstance(main_container, html.Div), "Main container should be a Div"
        
        # Look for RadioItems component
        radio_items_found = False
        radio_component = None
        
        def find_radio_items(element):
            """Recursively search for a RadioItems component."""
            if isinstance(element, dcc.RadioItems):
                return element
            
            if hasattr(element, 'children') and element.children is not None:
                if isinstance(element.children, list):
                    for child in element.children:
                        result = find_radio_items(child)
                        if result is not None:
                            return result
                else:
                    result = find_radio_items(element.children)
                    if result is not None:
                        return result
            
            return None
        
        radio_component = find_radio_items(main_container)
        assert radio_component is not None, "App layout should contain a dcc.RadioItems component for region filtering"
        
        # Verify the radio items has the correct id
        assert radio_component.id == 'region-filter', "RadioItems component should have id 'region-filter'"
        
        # Verify the options are present
        assert radio_component.options is not None, "RadioItems should have options"
        
        # Extract option values
        option_values = [opt['value'] for opt in radio_component.options]
        
        # Verify all 5 region options are present
        expected_options = {'all', 'north', 'south', 'east', 'west'}
        actual_options = set(option_values)
        
        assert actual_options == expected_options, (
            f"RadioItems should have options {expected_options}, but has {actual_options}"
        )
        
        # Verify default value is 'all'
        assert radio_component.value == 'all', "RadioItems default value should be 'all'"


class TestDashAppCallbacks:
    """Test suite for Dash app callbacks and interactivity."""
    
    def test_sales_chart_callback_exists(self):
        """
        Test that the sales chart callback is registered.
        Verifies the callback for region filtering is properly configured.
        """
        # Check that the callback function exists in the app module
        import app as app_module
        
        # Verify the update_chart function exists (the callback handler)
        assert hasattr(app_module, 'update_chart'), "App module should have update_chart callback function"
        
        # Verify it's callable
        assert callable(app_module.update_chart), "update_chart should be callable"


if __name__ == '__main__':
    pytest.main([__file__, '-v'])
