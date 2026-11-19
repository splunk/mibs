#
# PySNMP MIB module CISCO-VQE-TOOLS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-VQE-TOOLS-MIB
# Produced by pysmi-1.1.12 at Thu Nov 19 14:35:14 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, Integer32, Gauge32, MibIdentifier, NotificationType, Unsigned32, ObjectIdentity, IpAddress, iso, TimeTicks, Counter32, ModuleIdentity, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "Integer32", "Gauge32", "MibIdentifier", "NotificationType", "Unsigned32", "ObjectIdentity", "IpAddress", "iso", "TimeTicks", "Counter32", "ModuleIdentity", "Counter64")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoVqeToolsMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 969))
ciscoVqeToolsMIB.setRevisions(('2009-12-18 13:41',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoVqeToolsMIB.setRevisionsDescriptions(('Latest version of the MIB',))
if mibBuilder.loadTexts: ciscoVqeToolsMIB.setLastUpdated('200912181341Z')
if mibBuilder.loadTexts: ciscoVqeToolsMIB.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoVqeToolsMIB.setContactInfo('Cisco Systems\n            Customer Service\n\n            Postal: 170 W Tasman Drive\n            San Jose, CA  95134\n            USA\n\n            Tel: +1 800 553-NETS\n\n            E-mail: bxb-iptv-team@cisco.com')
if mibBuilder.loadTexts: ciscoVqeToolsMIB.setDescription('This MIB module defines a set of objects for monitoring the\n        VQE Client Channel Configuration Delivery Server (VCDS) \n        operational status: number of open connections, Real Time\n        Streaming Protocol (RTSP) reqests received and responses \n        sent from the VCDS.\n\n        Visual Quality Experience Tools Server(VQE-Tools) is\n        responsible for the creation, maintenance, and distribution \n        of the channel information containing channel-lineup data.')
ciscoVqeToolsMIBNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 969, 0))
ciscoVqeToolsMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 969, 1))
ciscoVqeToolsMIBConform = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 969, 2))
cvqtVcdsInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 969, 1, 1))
cvqtNumberOfSessions = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 969, 1, 1, 1), Gauge32()).setUnits('RTSP connections').setMaxAccess("readonly")
if mibBuilder.loadTexts: cvqtNumberOfSessions.setStatus('current')
if mibBuilder.loadTexts: cvqtNumberOfSessions.setDescription('This object indicates the number of open RTSP connections\n        between VCDS and RTSP clients.')
cvqtTotalReceivedRequests = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 969, 1, 1, 2), Counter64()).setUnits('RTSP requests').setMaxAccess("readonly")
if mibBuilder.loadTexts: cvqtTotalReceivedRequests.setStatus('current')
if mibBuilder.loadTexts: cvqtTotalReceivedRequests.setDescription('This object indicates the number of RTSP requests received\n        at VCDS.')
cvqtTotalSentResponses = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 969, 1, 1, 3), Counter64()).setUnits('RTSP responses').setMaxAccess("readonly")
if mibBuilder.loadTexts: cvqtTotalSentResponses.setStatus('current')
if mibBuilder.loadTexts: cvqtTotalSentResponses.setDescription('This object indicates the number of RTSP responses sent\n        from VCDS.')
cvqtRequestRate = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 969, 1, 1, 4), Gauge32()).setUnits('requests per second').setMaxAccess("readonly")
if mibBuilder.loadTexts: cvqtRequestRate.setStatus('current')
if mibBuilder.loadTexts: cvqtRequestRate.setDescription('This object indicates the number of RTSP requests received\n        at VCDS per second.')
cvqtMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 969, 2, 1))
cvqtMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 969, 2, 2))
cvqtMIBReadOnlyCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 969, 2, 1, 1)).setObjects(("CISCO-VQE-TOOLS-MIB", "ciscoVqeToolsVcdsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cvqtMIBReadOnlyCompliance = cvqtMIBReadOnlyCompliance.setStatus('current')
if mibBuilder.loadTexts: cvqtMIBReadOnlyCompliance.setDescription('The compliance statement for entities which implement this MIB.')
ciscoVqeToolsVcdsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 969, 2, 2, 1)).setObjects(("CISCO-VQE-TOOLS-MIB", "cvqtNumberOfSessions"), ("CISCO-VQE-TOOLS-MIB", "cvqtTotalReceivedRequests"), ("CISCO-VQE-TOOLS-MIB", "cvqtTotalSentResponses"), ("CISCO-VQE-TOOLS-MIB", "cvqtRequestRate"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVqeToolsVcdsGroup = ciscoVqeToolsVcdsGroup.setStatus('current')
if mibBuilder.loadTexts: ciscoVqeToolsVcdsGroup.setDescription('A collection of objects providing the VCDS stats\n        information.')
mibBuilder.exportSymbols("CISCO-VQE-TOOLS-MIB", ciscoVqeToolsVcdsGroup=ciscoVqeToolsVcdsGroup, cvqtMIBReadOnlyCompliance=cvqtMIBReadOnlyCompliance, ciscoVqeToolsMIB=ciscoVqeToolsMIB, ciscoVqeToolsMIBConform=ciscoVqeToolsMIBConform, cvqtRequestRate=cvqtRequestRate, ciscoVqeToolsMIBNotifs=ciscoVqeToolsMIBNotifs, cvqtVcdsInfo=cvqtVcdsInfo, cvqtTotalSentResponses=cvqtTotalSentResponses, cvqtMIBCompliances=cvqtMIBCompliances, cvqtMIBGroups=cvqtMIBGroups, PYSNMP_MODULE_ID=ciscoVqeToolsMIB, ciscoVqeToolsMIBObjects=ciscoVqeToolsMIBObjects, cvqtTotalReceivedRequests=cvqtTotalReceivedRequests, cvqtNumberOfSessions=cvqtNumberOfSessions)
