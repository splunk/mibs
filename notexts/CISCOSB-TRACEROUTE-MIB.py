#
# PySNMP MIB module CISCOSB-TRACEROUTE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCOSB-TRACEROUTE-MIB
# Produced by pysmi-1.1.12 at Thu Nov 26 06:06:58 2026
# On host runnervm0hi8g platform Linux version 7.0.0-1020-azure by user runner
# Using Python version 3.13.18 (main, Oct 26 2026, 14:19:33) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
switch001, = mibBuilder.importSymbols("CISCOSB-MIB", "switch001")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter64, TimeTicks, NotificationType, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, ModuleIdentity, IpAddress, Bits, Gauge32, Unsigned32, MibIdentifier, Counter32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "TimeTicks", "NotificationType", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "ModuleIdentity", "IpAddress", "Bits", "Gauge32", "Unsigned32", "MibIdentifier", "Counter32", "ObjectIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
rlTraceRoute = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 81))
rlTraceRoute.setRevisions(('2007-01-02 00:00',))
if mibBuilder.loadTexts: rlTraceRoute.setLastUpdated('200701020000Z')
if mibBuilder.loadTexts: rlTraceRoute.setOrganization('Cisco Systems, Inc.')
rlTraceRouteMibVersion = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 81, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlTraceRouteMibVersion.setStatus('current')
rlTraceRouteWebLastTestName = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 81, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlTraceRouteWebLastTestName.setStatus('current')
mibBuilder.exportSymbols("CISCOSB-TRACEROUTE-MIB", rlTraceRoute=rlTraceRoute, rlTraceRouteMibVersion=rlTraceRouteMibVersion, PYSNMP_MODULE_ID=rlTraceRoute, rlTraceRouteWebLastTestName=rlTraceRouteWebLastTestName)
