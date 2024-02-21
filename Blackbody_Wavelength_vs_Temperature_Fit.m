data = load('Wavelength_vs_Temperature.txt');
x_data = data(:, 1);
y_data = data(:, 2);
x_error = data(:, 3);
y_error = data(:, 4);

initial_guess = [2.898e-3]; % Initial parameter guesses

% Perform curve fitting with increased MaxIter
options = optimset('MaxIter', 350000000);  % Adjust the value as needed
fitted_params = lsqcurvefit(@single_slit_fit, initial_guess, x_data, y_data, [], [], options);

% Calculate uncertainties
[~, R, J] = nlinfit(x_data, y_data, @single_slit_fit, fitted_params);
ci = nlparci(fitted_params, R, 'Jacobian', J);
uncertainties = diff(ci) / 2;

% Calculate residuals
residuals = y_data - single_slit_fit(fitted_params, x_data);

% Define x_fit and y_fit with the same length
x_fit = linspace(min(x_data), max(x_data), 10000);
y_fit = single_slit_fit(fitted_params, x_fit);

% Plot the data with error bars and the fitted curve
figure;
errorbar(x_data, y_data, y_error, 'o', 'MarkerFaceColor', 'b', 'MarkerEdgeColor', 'b');
hold on;
plot(x_fit, y_fit, 'r', 'LineWidth', 2);
% Plot the curve y = 2898000/x
plot(x_fit, 0.002898./x_fit, 'g--', 'LineWidth', 2);
legend('Data', 'Best Fit', 'T = 2.898e-3/{\lambda_{max}}')
xlabel('Wavelength of Peak (nm)');
ylabel('Absolute Tempurature (K)');
title('Wien''s Displacement Law');

figure;
% Plot residuals with error bars
errorbar(x_data, residuals, y_error, 'o', 'MarkerFaceColor', 'b', 'MarkerEdgeColor', 'b');
hold on;
plot([min(x_data), max(x_data)], [0, 0], 'r', 'LineWidth', 2); % Add a red horizontal line at y = 0
xlabel('Wavelength of Peak (nm)');
ylabel('Residuals');
title('Residuals vs Wavelength');

for i = 1:numel(fitted_params)
    fprintf('Parameter %d: %.4f ± %.4f\n', i, fitted_params(i), uncertainties(i));
end

saveas(gcf, 'your_figure.png');
% Calculate chi-square statistic
chi_square = sum((residuals ./ y_error).^2);

% Calculate R-squared
y_mean = mean(y_data);
ss_total = sum((y_data - y_mean).^2);
ss_residual = sum(residuals.^2);
r_squared = 1 - (ss_residual / ss_total);

% Root Mean Square Error (RMSE)
rmse = sqrt(mean(residuals.^2));

fprintf('Chi-Square: %.4f\n', chi_square);
fprintf('R-squared: %.4f\n', r_squared);
fprintf('RMSE: %.4f\n', rmse);

% QQ Plot
figure;
qqplot(residuals);

% Example fitting function with parameters 'a', 'b', 'c', and 'd'
function y_fit = single_slit_fit(params, x)
    a = params(1);

    y_fit = (a ./ x);
end

