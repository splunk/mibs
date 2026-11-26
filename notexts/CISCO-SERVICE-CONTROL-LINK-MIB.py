#
# PySNMP MIB module CISCO-SERVICE-CONTROL-LINK-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-SERVICE-CONTROL-LINK-MIB
# Produced by pysmi-1.1.12 at Thu Nov 26 06:07:01 2026
# On host runnervm0hi8g platform Linux version 7.0.0-1020-azure by user runner
# Using Python version 3.13.18 (main, Oct 26 2026, 14:19:33) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
EntPhysicalIndexOrZero, = mibBuilder.importSymbols("CISCO-TC", "EntPhysicalIndexOrZero")
entPhysicalIndex, PhysicalIndex = mibBuilder.importSymbols("ENTITY-MIB", "entPhysicalIndex", "PhysicalIndex")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
Counter64, TimeTicks, NotificationType, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, ModuleIdentity, IpAddress, Bits, Gauge32, Unsigned32, MibIdentifier, Counter32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "TimeTicks", "NotificationType", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "ModuleIdentity", "IpAddress", "Bits", "Gauge32", "Unsigned32", "MibIdentifier", "Counter32", "ObjectIdentity")
DisplayString, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "TextualConvention")
ciscoServiceControlLinkMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 631))
ciscoServiceControlLinkMIB.setRevisions(('2007-06-26 00:00',))
if mibBuilder.loadTexts: ciscoServiceControlLinkMIB.setLastUpdated('200706260000Z')
if mibBuilder.loadTexts: ciscoServiceControlLinkMIB.setOrganization('Cisco Systems, Inc.')
ciscoSCLinkMIBNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 631, 0))
ciscoSCLinkMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 631, 1))
ciscoSCLinkMIBConform = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 631, 2))
class CsceLinkModeType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("other", 1), ("bypass", 2), ("forwarding", 3), ("cutoff", 4), ("sniffing", 5))

cscLinkNotifsEnabled = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 631, 1, 1), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cscLinkNotifsEnabled.setStatus('current')
cscLinkStatusTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 631, 1, 2), )
if mibBuilder.loadTexts: cscLinkStatusTable.setStatus('current')
cscLinkStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 631, 1, 2, 1), ).setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"))
if mibBuilder.loadTexts: cscLinkStatusEntry.setStatus('current')
cscLinkAdminModeOnActive = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 631, 1, 2, 1, 1), CsceLinkModeType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cscLinkAdminModeOnActive.setStatus('current')
cscLinkAdminModeOnFailure = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 631, 1, 2, 1, 2), CsceLinkModeType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cscLinkAdminModeOnFailure.setStatus('current')
cscLinkOperMode = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 631, 1, 2, 1, 3), CsceLinkModeType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cscLinkOperMode.setStatus('current')
cscLinkAdminReflectionEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 631, 1, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("reflectionEnabled", 1), ("reflectionOnAllPortsEnabled", 2), ("reflectionDisabled", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cscLinkAdminReflectionEnable.setStatus('current')
cscLinkSubscriberSidePortIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 631, 1, 2, 1, 5), EntPhysicalIndexOrZero()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cscLinkSubscriberSidePortIndex.setStatus('current')
cscLinkNetworkSidePortIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 631, 1, 2, 1, 6), EntPhysicalIndexOrZero()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cscLinkNetworkSidePortIndex.setStatus('current')
cscLinkAdminReflectionState = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 631, 1, 2, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("noLinkReflection", 1), ("reflectingFailureToNetwork", 2), ("reflectingFailureToSubscriber", 3), ("reflectingFailureToBoth", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cscLinkAdminReflectionState.setStatus('current')
ciscoServiceControlLinkModeChange = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 631, 0, 1)).setObjects(("CISCO-SERVICE-CONTROL-LINK-MIB", "cscLinkOperMode"))
if mibBuilder.loadTexts: ciscoServiceControlLinkModeChange.setStatus('current')
ciscoSCLinkMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 631, 2, 1))
ciscoSCLinkMIBObjectGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 631, 2, 2))
cServiceLinkMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 631, 2, 1, 1)).setObjects(("CISCO-SERVICE-CONTROL-LINK-MIB", "cSCLinkMIBObjectGroup"), ("CISCO-SERVICE-CONTROL-LINK-MIB", "cSCLinkMIBNotificationGroup"), ("CISCO-SERVICE-CONTROL-LINK-MIB", "cSCLinkNotifControlGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cServiceLinkMIBCompliance = cServiceLinkMIBCompliance.setStatus('current')
cSCLinkMIBObjectGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 631, 2, 2, 1)).setObjects(("CISCO-SERVICE-CONTROL-LINK-MIB", "cscLinkAdminModeOnActive"), ("CISCO-SERVICE-CONTROL-LINK-MIB", "cscLinkAdminModeOnFailure"), ("CISCO-SERVICE-CONTROL-LINK-MIB", "cscLinkOperMode"), ("CISCO-SERVICE-CONTROL-LINK-MIB", "cscLinkAdminReflectionEnable"), ("CISCO-SERVICE-CONTROL-LINK-MIB", "cscLinkSubscriberSidePortIndex"), ("CISCO-SERVICE-CONTROL-LINK-MIB", "cscLinkNetworkSidePortIndex"), ("CISCO-SERVICE-CONTROL-LINK-MIB", "cscLinkAdminReflectionState"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cSCLinkMIBObjectGroup = cSCLinkMIBObjectGroup.setStatus('current')
cSCLinkMIBNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 9, 9, 631, 2, 2, 2)).setObjects(("CISCO-SERVICE-CONTROL-LINK-MIB", "ciscoServiceControlLinkModeChange"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cSCLinkMIBNotificationGroup = cSCLinkMIBNotificationGroup.setStatus('current')
cSCLinkNotifControlGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 631, 2, 2, 3)).setObjects(("CISCO-SERVICE-CONTROL-LINK-MIB", "cscLinkNotifsEnabled"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cSCLinkNotifControlGroup = cSCLinkNotifControlGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-SERVICE-CONTROL-LINK-MIB", ciscoSCLinkMIBCompliances=ciscoSCLinkMIBCompliances, PYSNMP_MODULE_ID=ciscoServiceControlLinkMIB, cSCLinkMIBObjectGroup=cSCLinkMIBObjectGroup, cscLinkAdminModeOnFailure=cscLinkAdminModeOnFailure, ciscoSCLinkMIBConform=ciscoSCLinkMIBConform, cscLinkNotifsEnabled=cscLinkNotifsEnabled, cscLinkStatusTable=cscLinkStatusTable, ciscoSCLinkMIBObjects=ciscoSCLinkMIBObjects, cscLinkAdminReflectionEnable=cscLinkAdminReflectionEnable, cscLinkOperMode=cscLinkOperMode, cSCLinkMIBNotificationGroup=cSCLinkMIBNotificationGroup, cscLinkAdminModeOnActive=cscLinkAdminModeOnActive, cSCLinkNotifControlGroup=cSCLinkNotifControlGroup, ciscoSCLinkMIBNotifs=ciscoSCLinkMIBNotifs, ciscoServiceControlLinkModeChange=ciscoServiceControlLinkModeChange, cscLinkAdminReflectionState=cscLinkAdminReflectionState, CsceLinkModeType=CsceLinkModeType, cscLinkSubscriberSidePortIndex=cscLinkSubscriberSidePortIndex, ciscoSCLinkMIBObjectGroups=ciscoSCLinkMIBObjectGroups, cscLinkNetworkSidePortIndex=cscLinkNetworkSidePortIndex, ciscoServiceControlLinkMIB=ciscoServiceControlLinkMIB, cServiceLinkMIBCompliance=cServiceLinkMIBCompliance, cscLinkStatusEntry=cscLinkStatusEntry)
