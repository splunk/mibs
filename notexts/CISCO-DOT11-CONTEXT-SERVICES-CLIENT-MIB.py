#
# PySNMP MIB module CISCO-DOT11-CONTEXT-SERVICES-CLIENT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-DOT11-CONTEXT-SERVICES-CLIENT-MIB
# Produced by pysmi-1.1.12 at Thu Nov 26 06:07:00 2026
# On host runnervm0hi8g platform Linux version 7.0.0-1020-azure by user runner
# Using Python version 3.13.18 (main, Oct 26 2026, 14:19:33) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
ciscoExperiment, = mibBuilder.importSymbols("CISCO-SMI", "ciscoExperiment")
InetAddress, InetAddressType = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddress", "InetAddressType")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
Counter64, TimeTicks, NotificationType, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, ModuleIdentity, IpAddress, Bits, Gauge32, Unsigned32, MibIdentifier, Counter32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "TimeTicks", "NotificationType", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "ModuleIdentity", "IpAddress", "Bits", "Gauge32", "Unsigned32", "MibIdentifier", "Counter32", "ObjectIdentity")
TimeInterval, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "TimeInterval", "DisplayString", "TextualConvention")
ciscoDot11CscMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 10, 109))
ciscoDot11CscMIB.setRevisions(('2004-06-02 00:00', '2003-05-06 00:00',))
if mibBuilder.loadTexts: ciscoDot11CscMIB.setLastUpdated('200406020000Z')
if mibBuilder.loadTexts: ciscoDot11CscMIB.setOrganization('Cisco Systems Inc.')
ciscoDot11CscMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 109, 1))
ciscoDot11CscMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 109, 2))
ciscoDot11CscConfigGlobal = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 109, 1, 1))
cDot11CscAddressType = MibScalar((1, 3, 6, 1, 4, 1, 9, 10, 109, 1, 1, 1), InetAddressType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cDot11CscAddressType.setStatus('current')
cDot11CscParentWdsAddress = MibScalar((1, 3, 6, 1, 4, 1, 9, 10, 109, 1, 1, 2), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cDot11CscParentWdsAddress.setStatus('current')
cDot11CscRootNodeAddress = MibScalar((1, 3, 6, 1, 4, 1, 9, 10, 109, 1, 1, 3), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cDot11CscRootNodeAddress.setStatus('current')
cDot11CscMnAuthenticatorAddress = MibScalar((1, 3, 6, 1, 4, 1, 9, 10, 109, 1, 1, 4), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cDot11CscMnAuthenticatorAddress.setStatus('current')
cDot11CscOperMode = MibScalar((1, 3, 6, 1, 4, 1, 9, 10, 109, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("infrastructure", 1), ("distributed", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cDot11CscOperMode.setStatus('current')
cDot11CscMnInactivityTime = MibScalar((1, 3, 6, 1, 4, 1, 9, 10, 109, 1, 1, 6), TimeInterval()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cDot11CscMnInactivityTime.setStatus('current')
cDot11CscRegistrationLifeTime = MibScalar((1, 3, 6, 1, 4, 1, 9, 10, 109, 1, 1, 7), TimeInterval()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cDot11CscRegistrationLifeTime.setStatus('current')
cDot11CscStateTransitions = MibScalar((1, 3, 6, 1, 4, 1, 9, 10, 109, 1, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cDot11CscStateTransitions.setStatus('current')
ciscoDot11CscMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 109, 2, 1))
ciscoDot11CscMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 109, 2, 2))
ciscoDot11CscMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 10, 109, 2, 1, 1)).setObjects(("CISCO-DOT11-CONTEXT-SERVICES-CLIENT-MIB", "ciscoDot11CscConfigGlobalGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDot11CscMIBCompliance = ciscoDot11CscMIBCompliance.setStatus('current')
ciscoDot11CscConfigGlobalGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 10, 109, 2, 2, 1)).setObjects(("CISCO-DOT11-CONTEXT-SERVICES-CLIENT-MIB", "cDot11CscAddressType"), ("CISCO-DOT11-CONTEXT-SERVICES-CLIENT-MIB", "cDot11CscParentWdsAddress"), ("CISCO-DOT11-CONTEXT-SERVICES-CLIENT-MIB", "cDot11CscRootNodeAddress"), ("CISCO-DOT11-CONTEXT-SERVICES-CLIENT-MIB", "cDot11CscMnAuthenticatorAddress"), ("CISCO-DOT11-CONTEXT-SERVICES-CLIENT-MIB", "cDot11CscOperMode"), ("CISCO-DOT11-CONTEXT-SERVICES-CLIENT-MIB", "cDot11CscMnInactivityTime"), ("CISCO-DOT11-CONTEXT-SERVICES-CLIENT-MIB", "cDot11CscRegistrationLifeTime"), ("CISCO-DOT11-CONTEXT-SERVICES-CLIENT-MIB", "cDot11CscStateTransitions"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDot11CscConfigGlobalGroup = ciscoDot11CscConfigGlobalGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-DOT11-CONTEXT-SERVICES-CLIENT-MIB", cDot11CscMnInactivityTime=cDot11CscMnInactivityTime, ciscoDot11CscConfigGlobalGroup=ciscoDot11CscConfigGlobalGroup, ciscoDot11CscMIBObjects=ciscoDot11CscMIBObjects, cDot11CscAddressType=cDot11CscAddressType, cDot11CscRootNodeAddress=cDot11CscRootNodeAddress, cDot11CscRegistrationLifeTime=cDot11CscRegistrationLifeTime, ciscoDot11CscMIBGroups=ciscoDot11CscMIBGroups, cDot11CscStateTransitions=cDot11CscStateTransitions, ciscoDot11CscMIBConformance=ciscoDot11CscMIBConformance, cDot11CscMnAuthenticatorAddress=cDot11CscMnAuthenticatorAddress, ciscoDot11CscMIBCompliances=ciscoDot11CscMIBCompliances, ciscoDot11CscMIBCompliance=ciscoDot11CscMIBCompliance, cDot11CscParentWdsAddress=cDot11CscParentWdsAddress, cDot11CscOperMode=cDot11CscOperMode, PYSNMP_MODULE_ID=ciscoDot11CscMIB, ciscoDot11CscConfigGlobal=ciscoDot11CscConfigGlobal, ciscoDot11CscMIB=ciscoDot11CscMIB)
