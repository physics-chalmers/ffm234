% Make an x,y grid
[X,Y] = ndgrid(linspace(-2.5,2.5,100),linspace(-2.5,2.5,100));
R=sqrt(X.^2+Y.^2);

% Plot streamlines for corresponding vector field
v_x = - Y ./ R.^2; % Note that -Y/R = -sin(phi)
v_y = X ./ R.^2;   % Note that X/R = cos(phi)

% In Matlab we have to provide start points for streamlines.
start1_y=-2.0:0.5:-0.5;
start_y=[start1_y, -start1_y];
start_x=[zeros(size(start_y))];

% Fine tuning might be needed to get a nice set of streamlines.
strm=streamline(X', Y', v_x', v_y', start_x, start_y,[0.01]);
set(strm,'LineWidth',2,'Color','k')

hold on

% Matlab streamlines have no arrows. Combine with quiver.
% Use fewer grid points to avoid too many arrows in the plot.
[Xc,Yc] = ndgrid(linspace(-3,3,10),linspace(-3,3,10));
Rc=sqrt(Xc.^2+Yc.^2);
v_xc = - Yc ./ Rc.^2; % Note that -Y/R = -sin(phi)
v_yc = Xc ./ Rc.^2;   % Note that X/R = cos(phi)
qvr=quiver(Xc', Yc', v_xc', v_yc','Color','k');

xlabel('x')
ylabel('y')
xlim([-2.5,2.5])
ylim([-2.5,2.5])
