#
# PySNMP MIB module LINKSYS-TRACEROUTE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/linksys/LINKSYS-TRACEROUTE-MIB
# Produced by pysmi-1.1.12 at Thu Nov 19 14:38:11 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
rnd, = mibBuilder.importSymbols("LINKSYS-MIB", "rnd")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Gauge32, Counter64, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, ModuleIdentity, NotificationType, iso, Integer32, TimeTicks, Unsigned32, Counter32, IpAddress, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "Counter64", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "ModuleIdentity", "NotificationType", "iso", "Integer32", "TimeTicks", "Unsigned32", "Counter32", "IpAddress", "ObjectIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
rlTraceRoute = ModuleIdentity((1, 3, 6, 1, 4, 1, 3955, 1000, 201, 81))
rlTraceRoute.setRevisions(('2007-01-02 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: rlTraceRoute.setRevisionsDescriptions(('Initial revision.',))
if mibBuilder.loadTexts: rlTraceRoute.setLastUpdated('200701020000Z')
if mibBuilder.loadTexts: rlTraceRoute.setOrganization('\n                              Linksys LLC.')
if mibBuilder.loadTexts: rlTraceRoute.setContactInfo('www.linksys.com/business/support')
if mibBuilder.loadTexts: rlTraceRoute.setDescription('This private MIB module defines TRACE ROUTE private MIBs.')
rlTraceRouteMibVersion = MibScalar((1, 3, 6, 1, 4, 1, 3955, 1000, 201, 81, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlTraceRouteMibVersion.setStatus('current')
if mibBuilder.loadTexts: rlTraceRouteMibVersion.setDescription("MIB's version, the current version is 1.")
mibBuilder.exportSymbols("LINKSYS-TRACEROUTE-MIB", rlTraceRouteMibVersion=rlTraceRouteMibVersion, PYSNMP_MODULE_ID=rlTraceRoute, rlTraceRoute=rlTraceRoute)
