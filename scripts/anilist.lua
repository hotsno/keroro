local function check_completion()
    local pos = mp.get_property("percent-pos")
    if tonumber(pos) >= 80 then
        local command = "/path/to/python /path/to/update.py '" .. mp.get_property("path"):gsub("'", "'\\''") .. "'"
        os.execute(command)
        Timer:stop()
    end
end

local function start_timer()
    Timer:resume()
end

Timer = mp.add_periodic_timer(1, check_completion)
mp.register_event("start-file", start_timer)
