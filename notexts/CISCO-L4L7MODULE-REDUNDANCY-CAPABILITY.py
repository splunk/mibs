#
# PySNMP MIB module CISCO-L4L7MODULE-REDUNDANCY-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-L4L7MODULE-REDUNDANCY-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 26 06:07:00 2026
# On host runnervm0hi8g platform Linux version 7.0.0-1020-azure by user runner
# Using Python version 3.13.18 (main, Oct 26 2026, 14:19:33) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Counter64, TimeTicks, NotificationType, Integer32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, IpAddress, Bits, Gauge32, Unsigned32, MibIdentifier, Counter32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "TimeTicks", "NotificationType", "Integer32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "IpAddress", "Bits", "Gauge32", "Unsigned32", "MibIdentifier", "Counter32", "ObjectIdentity")
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
mibBuilder.exportSymbols("CISCO-L4L7MODULE-REDUNDANCY-CAPABILITY", cl4l7ModRedCapc4710aceVA3R100=cl4l7ModRedCapc4710aceVA3R100, ciscoL4l7moduleRedundancyCapability=ciscoL4l7moduleRedundancyCapability, PYSNMP_MODULE_ID=ciscoL4l7moduleRedundancyCapability)
