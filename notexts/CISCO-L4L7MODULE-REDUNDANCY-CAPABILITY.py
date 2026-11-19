#
# PySNMP MIB module CISCO-L4L7MODULE-REDUNDANCY-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-L4L7MODULE-REDUNDANCY-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 19 08:32:22 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
ModuleCompliance, NotificationGroup, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "AgentCapabilities")
ModuleIdentity, TimeTicks, IpAddress, Bits, ObjectIdentity, NotificationType, Gauge32, Counter64, Unsigned32, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Integer32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "TimeTicks", "IpAddress", "Bits", "ObjectIdentity", "NotificationType", "Gauge32", "Counter64", "Unsigned32", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Integer32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoL4l7moduleRedundancyCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 566))
ciscoL4l7moduleRedundancyCapability.setRevisions(('2008-07-23 00:00',))
if mibBuilder.loadTexts: ciscoL4l7moduleRedundancyCapability.setLastUpdated('200807230000Z')
if mibBuilder.loadTexts: ciscoL4l7moduleRedundancyCapability.setOrganization('Cisco Systems, Inc.')
cl4l7ModRedCapc4710aceVA3R100 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 566, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cl4l7ModRedCapc4710aceVA3R100 = cl4l7ModRedCapc4710aceVA3R100.setProductRelease('ACSW (Application Control Software) A3(1) for\n                     ACE 4710 Application Control Engine Appliance')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cl4l7ModRedCapc4710aceVA3R100 = cl4l7ModRedCapc4710aceVA3R100.setStatus('current')
mibBuilder.exportSymbols("CISCO-L4L7MODULE-REDUNDANCY-CAPABILITY", ciscoL4l7moduleRedundancyCapability=ciscoL4l7moduleRedundancyCapability, cl4l7ModRedCapc4710aceVA3R100=cl4l7ModRedCapc4710aceVA3R100, PYSNMP_MODULE_ID=ciscoL4l7moduleRedundancyCapability)
