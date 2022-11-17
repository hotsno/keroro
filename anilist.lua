local function check_completion()
    local pos = mp.get_property("percent-pos")
    if tonumber(pos) >= 80 then
        local command = python_path .. ' ' .. update_path .. ' "' .. mp.get_property("path") .. '"'
        os.execute(command)
        Timer:stop()
    end
end

local function start_timer()
    Timer:resume()
end

Timer = mp.add_periodic_timer(1, check_completion)
mp.register_event("start-file", start_timer)