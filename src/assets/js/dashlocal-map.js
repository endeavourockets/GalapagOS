var traj_path_positions;

var traj_path;
var wwd;
var pathsLayer;

setTimeout(() => {
    // Create a WorldWindow for the canvas.
    wwd = new WorldWind.WorldWindow("mapCanvas");

    // Add some image layers to the WorldWindow's globe.
    wwd.addLayer(new WorldWind.BMNGOneImageLayer());
    wwd.addLayer(new WorldWind.BMNGLandsatLayer());

    // Add a compass, a coordinates display and some view controls to the WorldWindow.
    wwd.addLayer(new WorldWind.CoordinatesDisplayLayer(wwd));
    wwd.addLayer(new WorldWind.ViewControlsLayer(wwd));

    //Initialize empty path
    traj_path_positions = [];

    traj_path = create_path(traj_path_positions);

    // Add the path to a layer and the layer to the WorldWindow's layer list.
    pathsLayer = new WorldWind.RenderableLayer();
    pathsLayer.displayName = "Paths";
    pathsLayer.addRenderable(traj_path);
    wwd.addLayer(pathsLayer);

    // Add a test trajectory at the Golden Gate Bridge
    add_to_path(new WorldWind.Position(37.8199, -122.478, 0));
    add_to_path(new WorldWind.Position(37.8199, -122.479, 100));
    add_to_path(new WorldWind.Position(37.8199, -122.48, 500));
    add_to_path(new WorldWind.Position(37.8199, -122.481, 1000));
    add_to_path(new WorldWind.Position(37.8199, -122.482, 3000));
    add_to_path(new WorldWind.Position(37.8199, -122.483, 1000));


    // remove loading symbol
    setTimeout(() => {
        document.querySelector('img.loading').classList.add('removed');
        auto_zoom();
    }, 500);
}, 2000);

function add_to_path(next_position){
    if(traj_path != null) pathsLayer.removeRenderable(traj_path);
    traj_path_positions.push(next_position);
    traj_path = create_path(traj_path_positions);
    pathsLayer.addRenderable(traj_path);

    pathsLayer.refresh();
    wwd.redraw();
}

function auto_zoom(){
     wwd.goTo(new WorldWind.Position(37.8199, -122.478, 3000))
}

function create_path(path_points){
    // Create the path.
    var newPath = new WorldWind.Path(path_points, null);
    newPath.altitudeMode = WorldWind.ABSOLUTE;
    newPath.followTerrain = false;
    newPath.extrude = false; // Make it a curtain.

    // Create and assign the path's attributes.
    var pathAttributes = new WorldWind.ShapeAttributes(null);
    pathAttributes.outlineColor = new WorldWind.Color(1, 0, 0, 1);
    pathAttributes.outlineWidth = 4;
    pathAttributes.drawInterior = true;
    pathAttributes.interiorColor = new WorldWind.Color(0.886, 0.204, 0.922, 1);
    //pathAttributes.drawVerticals = newPath.extrude; //Draw verticals only when extruding.
    newPath.attributes = pathAttributes;
    newPath.pathType = WorldWind.GREAT_CIRCLE;

    return newPath;
}
