clear a;
a = arduino();

function goforward(distance)
    factor = 5;
    if distance == 0
        % do nothing
    elseif distance > 0
        writeDigitalPin(a, 'D5', 1);
        pause(distance/factor)
        writeDigitalPin(a, 'D5', 0);
    else
        writeDigitalPin(a, 'D6', 1);
        pause(-distance/factor)
        writeDigitalPin(a, 'D6', 0);
    end
end