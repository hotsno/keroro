local msg = require("mp.msg")

local function check_completion()
    local pos = mp.get_property("percent-pos")
    mp.command_native_async({
			name = "subprocess",
			playback_only = false,
			args = {
				python_path,
				update_presence_path,
                mp.get_property("path"),
                pos
			},
		}, function() end)
    if tonumber(pos) >= 80 then
        local command = python_path .. ' ' .. update_path .. ' "' .. mp.get_property("path") .. '"'
        os.execute(command)
        Timer:stop()
    end
end

local cmd = nil

local function start_presence()
	if cmd == nil then
		cmd = mp.command_native_async({
			name = "subprocess",
			playback_only = false,
			args = {
				python_path,
				run_presence_path
			},
		}, function() end)
		msg.info("launched subprocess")
		mp.osd_message("Discord Rich Presence: Started")
	end
end

local function stop_presence()
	mp.abort_async_command(cmd)
	cmd = nil
	msg.info("aborted subprocess")
	mp.osd_message("Discord Rich Presence: Stopped")
end

local function start_timer()
    Timer:resume()
end

Timer = mp.add_periodic_timer(1, check_completion)

mp.register_event("start-file", function()
    start_timer()
    start_presence()
end)

mp.register_event("shutdown", function()
	if cmd ~= nil then
		stop_presence()
	end
end)
