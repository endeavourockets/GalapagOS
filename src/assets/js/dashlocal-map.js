setTimeout(() => {
    // Create a WorldWindow for the canvas.
    var wwd = new WorldWind.WorldWindow("mapCanvas");

    // Add some image layers to the WorldWindow's globe.
    wwd.addLayer(new WorldWind.BMNGOneImageLayer());
    wwd.addLayer(new WorldWind.BMNGLandsatLayer());

    // Add a compass, a coordinates display and some view controls to the WorldWindow.
    wwd.addLayer(new WorldWind.CompassLayer());
    wwd.addLayer(new WorldWind.CoordinatesDisplayLayer(wwd));
    wwd.addLayer(new WorldWind.ViewControlsLayer(wwd));

    // remove loading symbol
    setTimeout(() => {
        document.querySelector('img.loading').classList.add('removed');
    }, 500);
},2000);