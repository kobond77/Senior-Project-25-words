from HandTrackerRenderer import HandTrackerRenderer
from HandTrackerEdge import HandTracker

tracker = HandTracker(
        # Your own arguments
        ...
        )

renderer = HandTrackerRenderer(tracker=tracker)

while True:
    # Run hand tracker on next frame
    # 'bag' is some information common to the frame and to the hands 
    frame, hands, bag = tracker.next_frame()
    if frame is None: break
    # Draw hands
    frame = renderer.draw(frame, hands, bag)
    key = renderer.waitKey(delay=1)
    if key == 27 or key == ord('q'):
        break

renderer.exit()
tracker.exit()