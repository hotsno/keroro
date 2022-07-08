function check_completion()
    pos = mp.get_property("percent-pos")
    if tonumber(pos) >= 80 then
        command = "/path/to/python /path/to/update.py '" .. mp.get_property("path"):gsub("'", "'\\''") .. "'"
        os.execute(command)
        timer:stop()
    end
end

function start_timer()
    timer:resume()
end

timer = mp.add_periodic_timer(1, check_completion)
mp.register_event("start-file", start_timer)
