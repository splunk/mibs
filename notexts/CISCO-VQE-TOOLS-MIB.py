#
# PySNMP MIB module CISCO-VQE-TOOLS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-VQE-TOOLS-MIB
# Produced by pysmi-1.1.12 at Thu Nov 26 06:06:59 2026
# On host runnervm0hi8g platform Linux version 7.0.0-1020-azure by user runner
# Using Python version 3.13.18 (main, Oct 26 2026, 14:19:33) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
Counter64, TimeTicks, NotificationType, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, ModuleIdentity, IpAddress, Bits, Gauge32, Unsigned32, MibIdentifier, Counter32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "TimeTicks", "NotificationType", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "ModuleIdentity", "IpAddress", "Bits", "Gauge32", "Unsigned32", "MibIdentifier", "Counter32", "ObjectIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoVqeToolsMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 969))
ciscoVqeToolsMIB.setRevisions(('2009-12-18 13:41',))
if mibBuilder.loadTexts: ciscoVqeToolsMIB.setLastUpdated('200912181341Z')
if mibBuilder.loadTexts: ciscoVqeToolsMIB.setOrganization('Cisco Systems, Inc.')
ciscoVqeToolsMIBNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 969, 0))
ciscoVqeToolsMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 969, 1))
ciscoVqeToolsMIBConform = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 969, 2))
cvqtVcdsInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 969, 1, 1))
cvqtNumberOfSessions = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 969, 1, 1, 1), Gauge32()).setUnits('RTSP connections').setMaxAccess("readonly")
if mibBuilder.loadTexts: cvqtNumberOfSessions.setStatus('current')
cvqtTotalReceivedRequests = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 969, 1, 1, 2), Counter64()).setUnits('RTSP requests').setMaxAccess("readonly")
if mibBuilder.loadTexts: cvqtTotalReceivedRequests.setStatus('current')
cvqtTotalSentResponses = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 969, 1, 1, 3), Counter64()).setUnits('RTSP responses').setMaxAccess("readonly")
if mibBuilder.loadTexts: cvqtTotalSentResponses.setStatus('current')
cvqtRequestRate = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 969, 1, 1, 4), Gauge32()).setUnits('requests per second').setMaxAccess("readonly")
if mibBuilder.loadTexts: cvqtRequestRate.setStatus('current')
cvqtMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 969, 2, 1))
cvqtMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 969, 2, 2))
cvqtMIBReadOnlyCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 969, 2, 1, 1)).setObjects(("CISCO-VQE-TOOLS-MIB", "ciscoVqeToolsVcdsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cvqtMIBReadOnlyCompliance = cvqtMIBReadOnlyCompliance.setStatus('current')
ciscoVqeToolsVcdsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 969, 2, 2, 1)).setObjects(("CISCO-VQE-TOOLS-MIB", "cvqtNumberOfSessions"), ("CISCO-VQE-TOOLS-MIB", "cvqtTotalReceivedRequests"), ("CISCO-VQE-TOOLS-MIB", "cvqtTotalSentResponses"), ("CISCO-VQE-TOOLS-MIB", "cvqtRequestRate"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVqeToolsVcdsGroup = ciscoVqeToolsVcdsGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-VQE-TOOLS-MIB", cvqtMIBReadOnlyCompliance=cvqtMIBReadOnlyCompliance, ciscoVqeToolsMIBConform=ciscoVqeToolsMIBConform, ciscoVqeToolsVcdsGroup=ciscoVqeToolsVcdsGroup, cvqtTotalSentResponses=cvqtTotalSentResponses, cvqtRequestRate=cvqtRequestRate, ciscoVqeToolsMIBObjects=ciscoVqeToolsMIBObjects, cvqtMIBGroups=cvqtMIBGroups, PYSNMP_MODULE_ID=ciscoVqeToolsMIB, cvqtVcdsInfo=cvqtVcdsInfo, cvqtTotalReceivedRequests=cvqtTotalReceivedRequests, cvqtMIBCompliances=cvqtMIBCompliances, ciscoVqeToolsMIB=ciscoVqeToolsMIB, cvqtNumberOfSessions=cvqtNumberOfSessions, ciscoVqeToolsMIBNotifs=ciscoVqeToolsMIBNotifs)
